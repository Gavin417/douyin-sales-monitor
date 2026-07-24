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
anomaly = pd.read_csv("outputs/anomaly_report.csv")
top = pd.read_csv("outputs/dashboard_top_products.csv")

daily["sales_date"] = pd.to_datetime(daily["sales_date"])
anomaly["sales_date"] = pd.to_datetime(anomaly["sales_date"])

# ==========================
# Sidebar
# ==========================

st.sidebar.header("📊 Filters")

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

if product_search != "":
    top = top[
        top["product_name"]
            .str.contains(
                product_search,
                case=False,
                na=False
            )
    ]

    anomaly = anomaly[
        anomaly["product_name"]
            .str.contains(
                product_search,
                case=False,
                na=False
            )
    ]

anomaly_type = st.sidebar.selectbox(
    "Anomaly Type",
    [
        "All",
        "SALES_SPIKE",
        "SALES_DROP",
        "ZERO_SALES_AFTER_ACTIVE",
        "CAMPAIGN_SPIKE",
        "HIGH_VOLATILITY"
    ]
)

top_n = st.sidebar.slider(
    "Top Products",
    5,
    50,
    20
)

if len(date_range) == 2:

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    daily = daily[
        (daily["sales_date"] >= start_date)
        & (daily["sales_date"] <= end_date)
    ]

    anomaly = anomaly[
        (anomaly["sales_date"] >= start_date)
        & (anomaly["sales_date"] <= end_date)
    ]

if anomaly_type != "All":

    anomaly = anomaly[
        anomaly["anomaly_type"] == anomaly_type
    ]

if product_search.strip():

    anomaly = anomaly[
        anomaly["product_name"]
        .str.contains(
            product_search,
            case=False,
            na=False
        )
    ]
# -----------------------------
# KPI Cards
# -----------------------------
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Sales Spike",
    len(anomaly[anomaly["anomaly_type"] == "SALES_SPIKE"])
)

c2.metric(
    "Sales Drop",
    len(anomaly[anomaly["anomaly_type"] == "SALES_DROP"])
)

c3.metric(
    "Zero Sales",
    len(anomaly[anomaly["anomaly_type"] == "ZERO_SALES_AFTER_ACTIVE"])
)

c4.metric(
    "Campaign Spike",
    len(anomaly[anomaly["anomaly_type"] == "CAMPAIGN_SPIKE"])
)

c5.metric(
    "High Volatility",
    len(anomaly[anomaly["anomaly_type"] == "HIGH_VOLATILITY"])
)

st.divider()
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

drop_month = anomaly[
    anomaly["anomaly_type"] == "SALES_DROP"
].copy()

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

spike_month = anomaly[
    anomaly["anomaly_type"] == "SALES_SPIKE"
].copy()

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

anomaly_table = anomaly.copy()

if anomaly_type != "All":
    anomaly_table = anomaly_table[
        anomaly_table["anomaly_type"] == anomaly_type
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
