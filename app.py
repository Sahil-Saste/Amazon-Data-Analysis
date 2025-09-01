import streamlit as st
import pandas as pd
import altair as alt

# Load cleaned data
df = pd.read_csv("outputs/amazon_sales_clean.csv", parse_dates=["order_date"])

st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")
st.title("📊 Amazon Sales Dashboard")

# -------------------
# Detect important columns
# -------------------
def find_col(possible_names):
    for c in df.columns:
        for n in possible_names:
            if n in c.lower():
                return c
    return None

order_col = find_col(["order id", "orderid", "id"])
sku_col = find_col(["sku", "asin", "product"])
cat_col = find_col(["category", "product category"])
state_col = find_col(["state", "region"])
return_col = find_col(["return", "refund"])
delivered_col = find_col(["delivery status", "delivered", "ship status"])

# -------------------
# Sidebar Filters
# -------------------
st.sidebar.header("🔍 Filters")

# Date filter
if "order_date" in df.columns:
    min_date = df["order_date"].min()
    max_date = df["order_date"].max()
    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
    if len(date_range) == 2:
        df = df[(df["order_date"] >= pd.to_datetime(date_range[0])) & (df["order_date"] <= pd.to_datetime(date_range[1]))]

# Category filter
if cat_col:
    categories = st.sidebar.multiselect("Select Categories", df[cat_col].dropna().unique(), default=df[cat_col].dropna().unique())
    df = df[df[cat_col].isin(categories)]

# State filter
if state_col:
    states = st.sidebar.multiselect("Select States", df[state_col].dropna().unique(), default=df[state_col].dropna().unique())
    df = df[df[state_col].isin(states)]

# -------------------
# KPIs
# -------------------
total_revenue = df["revenue"].sum()
total_orders = df[order_col].nunique() if order_col else len(df)
aov = total_revenue / total_orders if total_orders else 0

# Returns
returns = None
if return_col:
    if df[return_col].dtype in ["int64", "float64"]:
        returns = int(df[return_col].sum())
    else:
        df[return_col] = df[return_col].astype(str)
        returns = df[return_col].str.lower().eq("returned").sum()

# Delivery Rate
delivery_rate = None
if delivered_col:
    if df[delivered_col].dtype in ["int64", "float64"]:
        delivery_rate = df[delivered_col].mean() * 100
    else:
        df[delivered_col] = df[delivered_col].astype(str)
        delivery_rate = (df[delivered_col].str.lower().eq("delivered").mean() * 100)

# Show KPIs
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("AOV", f"₹{aov:,.2f}")
col4.metric("Returns", f"{returns:,}" if returns is not None else "N/A")
col5.metric("Delivery Rate", f"{delivery_rate:.1f}%" if delivery_rate is not None else "N/A")

# -------------------
# Chart 1: Daily Revenue Trend
# -------------------
if "order_date" in df.columns:
    daily = df.groupby("order_date").agg({"revenue":"sum"}).reset_index()
    chart1 = alt.Chart(daily).mark_line(color="steelblue").encode(x="order_date:T", y="revenue:Q")
    st.subheader("📈 Daily Revenue Trend")
    st.altair_chart(chart1, use_container_width=True)

# -------------------
# Chart 2: Monthly Revenue Trend
# -------------------
if "order_date" in df.columns:
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    monthly = df.groupby("month").agg({"revenue":"sum"}).reset_index()
    chart2 = alt.Chart(monthly).mark_bar(color="purple").encode(x="month:N", y="revenue:Q")
    st.subheader("📅 Monthly Revenue Trend")
    st.altair_chart(chart2, use_container_width=True)

# -------------------
# Chart 3: Top 10 SKUs
# -------------------
if sku_col:
    top_skus = df.groupby(sku_col)["revenue"].sum().reset_index().sort_values("revenue", ascending=False).head(10)
    chart3 = alt.Chart(top_skus).mark_bar(color="orange").encode(x="revenue:Q", y=alt.Y(sku_col, sort="-x"))
    st.subheader("🏆 Top 10 SKUs by Revenue")
    st.altair_chart(chart3, use_container_width=True)

# -------------------
# Chart 4: Top Categories
# -------------------
if cat_col:
    top_cats = df.groupby(cat_col)["revenue"].sum().reset_index().sort_values("revenue", ascending=False).head(10)
    chart4 = alt.Chart(top_cats).mark_bar(color="teal").encode(x="revenue:Q", y=alt.Y(cat_col, sort="-x"))
    st.subheader("📦 Top Categories by Revenue")
    st.altair_chart(chart4, use_container_width=True)

# -------------------
# Chart 5: State Analysis
# -------------------
if state_col:
    state_agg = df.groupby(state_col)["revenue"].sum().reset_index().sort_values("revenue", ascending=False).head(10)
    chart5 = alt.Chart(state_agg).mark_bar(color="crimson").encode(x="revenue:Q", y=alt.Y(state_col, sort="-x"))
    st.subheader("🌍 Top 10 States by Revenue")
    st.altair_chart(chart5, use_container_width=True)
