import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="E-commerce Analytics", page_icon="📊", layout="wide")
st.title("E-commerce Sales & Customer Analytics")
st.caption("Portfolio demonstration using synthetic sample data, not real company results.")

@st.cache_data
def load_data():
    d = pd.read_csv(Path(__file__).parent / "data" / "ecommerce_orders.csv", parse_dates=["order_date"])
    d["revenue"] = d.quantity * d.unit_price * (1 - d.discount)
    return d

df = load_data()
with st.sidebar:
    st.header("Filters")
    date_range = st.date_input("Order date range", (df.order_date.min().date(), df.order_date.max().date()))
    categories = st.multiselect("Category", sorted(df.category.unique()), default=sorted(df.category.unique()))
    cities = st.multiselect("City", sorted(df.city.unique()), default=sorted(df.city.unique()))

if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = date_range
else:
    start, end = df.order_date.min().date(), df.order_date.max().date()
f = df[(df.order_date.dt.date >= start) & (df.order_date.dt.date <= end)]
f = f[f.category.isin(categories) & f.city.isin(cities)]
delivered = f[f.order_status == "Delivered"]
orders = delivered.order_id.nunique()
aov = delivered.groupby("order_id").revenue.sum().mean() if orders else 0

a,b,c,d = st.columns(4)
a.metric("Delivered revenue", f"₹{delivered.revenue.sum():,.0f}")
b.metric("Delivered orders", f"{orders:,}")
c.metric("Unique customers", f"{delivered.customer_id.nunique():,}")
d.metric("Average order value", f"₹{aov:,.0f}")

left,right = st.columns(2)
monthly = delivered.assign(month=delivered.order_date.dt.to_period("M").astype(str)).groupby("month", as_index=False).revenue.sum()
left.subheader("Monthly delivered revenue")
left.plotly_chart(px.line(monthly, x="month", y="revenue", markers=True), use_container_width=True)
category = delivered.groupby("category", as_index=False).revenue.sum().sort_values("revenue", ascending=False)
right.subheader("Revenue by category")
right.plotly_chart(px.bar(category, x="category", y="revenue"), use_container_width=True)

left,right = st.columns(2)
city = delivered.groupby("city", as_index=False).revenue.sum().sort_values("revenue", ascending=False)
left.subheader("Revenue by city")
left.plotly_chart(px.bar(city, x="city", y="revenue"), use_container_width=True)
status = f.order_status.value_counts().rename_axis("status").reset_index(name="orders")
right.subheader("Order status mix")
right.plotly_chart(px.pie(status, names="status", values="orders", hole=.4), use_container_width=True)

st.subheader("Top 10 customers by delivered spend")
top = delivered.groupby("customer_id", as_index=False).agg(total_spend=("revenue","sum"), orders=("order_id","nunique")).sort_values("total_spend", ascending=False).head(10)
st.dataframe(top, use_container_width=True, hide_index=True)
st.download_button("Download filtered data", f.to_csv(index=False).encode(), "filtered_orders.csv", "text/csv")
