import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "ecommerce_orders.csv", parse_dates=["order_date"])
df = df.drop_duplicates(subset=["order_id"])
df = df[df["quantity"] > 0].copy()
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
delivered = df[df["order_status"] == "Delivered"].copy()

out = ROOT / "reports"
out.mkdir(exist_ok=True)
kpis = pd.DataFrame([{
    "delivered_revenue": round(delivered.revenue.sum(), 2),
    "delivered_orders": int(delivered.order_id.nunique()),
    "unique_customers": int(delivered.customer_id.nunique()),
    "average_order_value": round(delivered.groupby("order_id").revenue.sum().mean(), 2),
    "delivery_rate_pct": round(df.order_status.eq("Delivered").mean() * 100, 2),
    "return_rate_pct": round(df.order_status.eq("Returned").mean() * 100, 2),
    "cancellation_rate_pct": round(df.order_status.eq("Cancelled").mean() * 100, 2)
}])
kpis.to_csv(out / "kpi_summary.csv", index=False)
(delivered.assign(month=delivered.order_date.dt.to_period("M").astype(str))
 .groupby("month", as_index=False).revenue.sum()
 .to_csv(out / "monthly_sales.csv", index=False))
(delivered.groupby("category", as_index=False)
 .agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"), units=("quantity", "sum"))
 .sort_values("revenue", ascending=False).to_csv(out / "category_performance.csv", index=False))
(delivered.groupby("customer_id", as_index=False)
 .agg(total_spend=("revenue", "sum"), order_count=("order_id", "nunique"))
 .sort_values("total_spend", ascending=False).to_csv(out / "customer_value.csv", index=False))
print(kpis.to_string(index=False))
print("Reports saved in reports/")
