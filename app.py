import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sales Anomaly Dashboard",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📈 Sales Anomaly Dashboard")

st.markdown("""
Monitor abnormal sales behaviour using automated anomaly detection.

Spike Detection • Drop Detection • Zero Sales Detection
""")

# -----------------------------
# Load Dashboard Summary
# -----------------------------
summary = pd.read_csv("outputs/dashboard_summary.csv")
daily = pd.read_csv("outputs/dashboard_daily_sales.csv")

spike = pd.read_csv("outputs/sales_spike.csv")
drop = pd.read_csv("outputs/sales_drop.csv")

top = pd.read_csv("outputs/dashboard_top_products.csv")

# ==========================
# Sidebar
# ==========================

st.sidebar.header("📊 Filters")

daily["sales_date"] = pd.to_datetime(daily["sales_date"])

date_range = st.sidebar.date_input(
    "Date Range",
    [
        daily["sales_date"].min(),
        daily["sales_date"].max()
    ]
)

product_search = st.sidebar.text_input(
    "Search Product",
    ""
)

anomaly_type = st.sidebar.selectbox(
    "Anomaly Type",
    [
        "All",
        "Spike",
        "Drop",
        "Zero"
    ]
)

top_n = st.sidebar.slider(
    "Top Products",
    5,
    50,
    20
)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    int(summary.loc[0, "total_records"])
)

col2.metric(
    "Products",
    int(summary.loc[0, "total_products"])
)

col3.metric(
    "Average Daily Sales",
    round(summary.loc[0, "avg_daily_sales"], 2)
)

col4.metric(
    "Total Sales",
    int(summary.loc[0, "total_sales"])
)

st.divider()

st.subheader("🚨 Anomaly Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Sales Spike",
    int(summary["total_spike"][0])
)

c2.metric(
    "Sales Drop",
    int(summary["total_drop"][0])
)

# 你的 summary 里目前没有 zero_sales，
# 先显示 0，后面我们再补上。
c3.metric(
    "Zero Sales",
    int(summary["total_zero"][0])
)
# -----------------------------
# Daily Sales Trend
# -----------------------------
st.markdown("---")

st.subheader("📈 Daily Sales Trend")

daily = pd.read_csv("outputs/dashboard_daily_sales.csv")

fig = px.line(
    daily,
    x="sales_date",
    y="daily_quantity",
    title="Daily Sales"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("📉 Drop Analysis")

drop_month = drop.copy()

drop_month["sales_date"] = pd.to_datetime(
    drop_month["sales_date"]
)

drop_month["month"] = (
    drop_month["sales_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_drop = (
    drop_month
    .groupby("month")
    .size()
    .reset_index(name="Drop Count")
)

fig_drop = px.bar(
    monthly_drop,
    x="month",
    y="Drop Count",
    title="Monthly Drop Count"
)

st.plotly_chart(
    fig_drop,
    use_container_width=True
)

# -----------------------------
# Top Products
# -----------------------------
st.markdown("---")

st.subheader("🏆 Top 20 Products")

top = pd.read_csv(
    "outputs/dashboard_top_products.csv"
)

top["short_name"] = (
    top["product_name"]
    .str.slice(0, 20)
    + "..."
)

top_chart = top.sort_values(
    "daily_quantity",
    ascending=True
)

fig2 = px.bar(
    top_chart,
    x="daily_quantity",
    y="short_name",
    orientation="h",
    title="Top Products by Total Sales",
    hover_data={
        "product_name": True,
        "short_name": False,
        "daily_quantity": ":,"
    }
)

fig2.update_layout(
    height=700,
    xaxis_title="Total Sales",
    yaxis_title="Product",
    showlegend=False
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------
# Top Products
# ------------------------
st.markdown("---")

st.subheader("📊 Spike Analysis")

spike_month = spike.copy()

spike_month["sales_date"] = pd.to_datetime(
    spike_month["sales_date"]
)

spike_month["month"] = (
    spike_month["sales_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_spike = (
    spike_month
    .groupby("month")
    .size()
    .reset_index(name="Spike Count")
)

fig_spike = px.bar(
    monthly_spike,
    x="month",
    y="Spike Count",
    title="Monthly Spike Count"
)

st.plotly_chart(
    fig_spike,
    use_container_width=True
)

# ==========================
# Anomaly Details
# ==========================

st.markdown("---")

st.subheader("📋 Anomaly Details")

spike_table = spike.copy()
drop_table = drop.copy()

spike_table["Type"] = "Spike"
drop_table["Type"] = "Drop"

spike_table = spike_table.rename(
    columns={
        "spike_ratio": "Ratio"
    }
)

drop_table = drop_table.rename(
    columns={
        "drop_ratio": "Ratio"
    }
)

anomaly_table = pd.concat(
    [spike_table, drop_table],
    ignore_index=True
)

anomaly_table = anomaly_table[
    [
        "sales_date",
        "product_name",
        "Type",
        "Ratio"
    ]
]

anomaly_table = anomaly_table.sort_values(
    "sales_date",
    ascending=False
)

st.dataframe(
    anomaly_table.reset_index(drop=True),
    use_container_width=True,
    height=500
)
