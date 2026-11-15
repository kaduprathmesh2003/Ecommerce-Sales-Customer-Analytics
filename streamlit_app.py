import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="E-commerce Analytics", page_icon="📊", layout="wide")
st.title("E-commerce Sales & Customer Analytics")
st.caption("Portfolio demonstration using synthetic sample data. Figures are illustrative, not real company results.")

@st.cache_data
def load_data():
    d = pd.read_csv(Path(__file__).parent / "data" / "ecommerce_orders.csv", parse_dates=["order_date"])
    d["revenue"] = d["quantity"] * d["unit_price"] * (1 - d["discount"])
    return d

df = load_data()
with st.sidebar:
    st.header("Report filters")
    date_range = st.date_input("Order date range", value=(df.order_date.min().date(), df.order_date.max().date()))
    categories = st.multiselect("Category", sorted(df.category.dropna().unique()), default=sorted(df.category.dropna().unique()))
    cities = st.multiselect("City", sorted(df.city.dropna().unique()), default=sorted(df.city.dropna().unique()))
    methods = st.multiselect("Payment method", sorted(df.payment_method.dropna().unique()), default=sorted(df.payment_method.dropna().unique()))

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start, end = date_range
else:
    start, end = df.order_date.min().date(), df.order_date.max().date()

f = df[
    df.order_date.dt.date.between(start, end)
    & df.category.isin(categories)
    & df.city.isin(cities)
    & df.payment_method.isin(methods)
].copy()
delivered = f[f.order_status.eq("Delivered")].copy()
total_orders = f.order_id.nunique()
delivered_orders = delivered.order_id.nunique()
delivered_revenue = delivered.revenue.sum()
aov = delivered.groupby("order_id").revenue.sum().mean() if delivered_orders else 0
unique_customers = delivered.customer_id.nunique()
delivery_rate = delivered_orders / total_orders if total_orders else 0
cancel_rate = f.loc[f.order_status.eq("Cancelled"), "order_id"].nunique() / total_orders if total_orders else 0
return_rate = f.loc[f.order_status.eq("Returned"), "order_id"].nunique() / total_orders if total_orders else 0

k1,k2,k3,k4 = st.columns(4)
k1.metric("Delivered revenue", f"₹{delivered_revenue:,.0f}")
k2.metric("Delivered orders", f"{delivered_orders:,}")
k3.metric("Unique customers", f"{unique_customers:,}")
k4.metric("Average order value", f"₹{aov:,.0f}")
st.caption(f"Filtered orders: {total_orders:,} · Delivered rate: {delivery_rate:.1%} · Cancellation rate: {cancel_rate:.1%} · Return rate: {return_rate:.1%}")

overview, customers, products, quality, data_tab = st.tabs([
    "Executive overview", "Customer insights", "Product & geography", "Order quality", "Data explorer"
])

with overview:
    left, right = st.columns(2)
    monthly = delivered.assign(month=delivered.order_date.dt.to_period("M").astype(str)).groupby("month", as_index=False).revenue.sum()
    left.subheader("Monthly delivered revenue")
    left.plotly_chart(px.line(monthly, x="month", y="revenue", markers=True, title="Revenue by month"), use_container_width=True)
    category = delivered.groupby("category", as_index=False).revenue.sum().sort_values("revenue", ascending=False)
    right.subheader("Delivered revenue by category")
    right.plotly_chart(px.bar(category, x="category", y="revenue", title="Revenue by category"), use_container_width=True)

with customers:
    st.subheader("Highest-value customers")
    top = delivered.groupby("customer_id", as_index=False).agg(
        delivered_spend=("revenue", "sum"), delivered_orders=("order_id", "nunique")
    ).sort_values("delivered_spend", ascending=False).head(10)
    left, right = st.columns(2)
    left.plotly_chart(px.bar(top.sort_values("delivered_spend"), x="delivered_spend", y="customer_id", orientation="h", title="Top 10 customers by spend"), use_container_width=True)
    right.plotly_chart(px.bar(top.sort_values("delivered_orders"), x="delivered_orders", y="customer_id", orientation="h", title="Top 10 customers by delivered orders"), use_container_width=True)
    st.dataframe(top, use_container_width=True, hide_index=True)

with products:
    left, right = st.columns(2)
    product = delivered.groupby("product", as_index=False).revenue.sum().sort_values("revenue", ascending=False)
    city = delivered.groupby("city", as_index=False).revenue.sum().sort_values("revenue", ascending=False)
    left.plotly_chart(px.bar(product, x="revenue", y="product", orientation="h", title="Revenue by product"), use_container_width=True)
    right.plotly_chart(px.bar(city, x="revenue", y="city", orientation="h", title="Revenue by city"), use_container_width=True)
    matrix = delivered.groupby(["category", "product"], as_index=False).agg(
        revenue=("revenue", "sum"), orders=("order_id", "nunique"), units=("quantity", "sum")
    ).sort_values("revenue", ascending=False)
    st.subheader("Category and product performance")
    st.dataframe(matrix, use_container_width=True, hide_index=True)

with quality:
    q1,q2,q3 = st.columns(3)
    q1.metric("Delivered rate", f"{delivery_rate:.1%}")
    q2.metric("Cancelled rate", f"{cancel_rate:.1%}")
    q3.metric("Returned rate", f"{return_rate:.1%}")
    left, right = st.columns(2)
    status = f.groupby("order_status", as_index=False).order_id.nunique().rename(columns={"order_id":"orders"})
    left.plotly_chart(px.pie(status, names="order_status", values="orders", hole=.45, title="Order status mix"), use_container_width=True)
    payment = f.groupby("payment_method", as_index=False).order_id.nunique().rename(columns={"order_id":"orders"})
    right.plotly_chart(px.bar(payment, x="payment_method", y="orders", title="Orders by payment method"), use_container_width=True)

with data_tab:
    st.subheader("Filtered order records")
    st.dataframe(f, use_container_width=True, hide_index=True)
    st.download_button("Download filtered CSV", f.to_csv(index=False).encode("utf-8"), "filtered_ecommerce_orders.csv", "text/csv")

st.divider()
st.caption("Data note: synthetic dataset. No cost, profit, marketing spend, acquisition channel, traffic or inventory fields are provided; profit, margin, ROAS, CAC and inventory metrics are intentionally excluded.")
