# 📊 Sales Anomaly Dashboard

> An interactive Streamlit dashboard for automated sales anomaly detection and business monitoring.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

---

# 📌 Project Overview

Retail businesses generate thousands of sales records every day. Manually identifying abnormal sales behaviour across hundreds of products is inefficient and often impossible.

This project builds an **automated anomaly detection system** that continuously monitors daily sales and highlights unusual business events through an interactive dashboard.

The system automatically detects:

- 📈 Sales Spike
- 📉 Sales Drop
- 🚫 Zero Sales
- 🏆 Top Selling Products
- 📊 Monthly Anomaly Trends

The final result is a business-friendly dashboard that enables analysts and managers to quickly discover abnormal sales behaviour and make data-driven decisions.

---

# 🎯 Objectives

The goal of this project is to:

- Monitor daily product sales
- Detect abnormal sales behaviour automatically
- Visualize sales trends
- Identify top-performing products
- Support business decision making
- Build an interactive dashboard for business users

---

# 📂 Dataset Summary

| Metric | Value |
|--------|-------|
| Total Records | **24,287** |
| Products | **660** |
| Total Sales | **115,479** |
| Time Range | **Dec 2024 – Jan 2026** |

---

# 🏗 Project Workflow

```text
                 Daily Sales Data
                        │
                        ▼
               Data Cleaning
                        │
                        ▼
           Feature Engineering
                        │
                        ▼
         Rolling Mean Calculation
                        │
                        ▼
       Spike / Drop Detection Logic
                        │
                        ▼
        Monthly Aggregation & KPIs
                        │
                        ▼
             CSV Output Files
                        │
                        ▼
        Interactive Streamlit Dashboard
```

---

# 📊 Dashboard Features

## 1️⃣ KPI Summary

The dashboard provides overall business statistics.

- Total Records
- Products
- Average Daily Sales
- Total Sales

---

## 2️⃣ Daily Sales Trend

Interactive Plotly line chart showing:

- Daily sales trend
- Seasonal patterns
- Long-term sales behaviour

Business users can quickly identify unusual sales periods.

---

## 3️⃣ Monthly Spike Analysis

Displays the number of detected sales spikes each month.

Useful for:

- Promotion evaluation
- Seasonal demand analysis
- Marketing effectiveness

---

## 4️⃣ Monthly Drop Analysis

Displays the number of detected sales drops each month.

Useful for:

- Inventory monitoring
- Supply chain issues
- Product performance tracking

---

## 5️⃣ Top Products

Ranks the highest-selling products.

Features:

- Horizontal ranking
- Hover to display full product name
- Easy product comparison

---

## 6️⃣ Anomaly Detail Table

Interactive searchable table containing:

- Sales Date
- Product Name
- Anomaly Type
- Spike / Drop Ratio

Users can sort and search anomalies for further investigation.

---

# 🧮 Anomaly Detection Method

The project uses a statistical rolling-window approach.

For every product:

### Step 1

Calculate a **7-day rolling average**

```text
Rolling Mean = Average(Sales over previous 7 days)
```

---

### Step 2

Compare today's sales with the rolling average.

---

### Step 3

Classify anomalies.

## 📈 Sales Spike

Current sales significantly exceed the rolling average.

Example:

Rolling Mean = 20

Today's Sales = 80

Spike Ratio = 4.0

---

## 📉 Sales Drop

Current sales fall significantly below the rolling average.

Example:

Rolling Mean = 40

Today's Sales = 2

Drop Ratio = 0.05

---

## 🚫 Zero Sales

Current sales equal zero.

---

# 📁 Project Structure

```text
sales-anomaly-dashboard/

│
├── app.py                     # Streamlit dashboard
├── dashboard.py
├── README.md
├── REPORT.md
├── requirements.txt
│
├── anomaly_detection/
│
├── outputs/
│   ├── dashboard_summary.csv
│   ├── dashboard_daily_sales.csv
│   ├── dashboard_top_products.csv
│   ├── dashboard_monthly_spikes.csv
│   ├── dashboard_monthly_drops.csv
│   ├── sales_spike.csv
│   └── sales_drop.csv
│
├── charts/
│
├── sql/
│
├── src/
│
└── logs/
```

---

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly |
| Database | PostgreSQL |
| Version Control | Git |
| Repository | GitHub |

---

# 📈 Business Insights

The dashboard enables business users to:

- Monitor abnormal sales automatically
- Detect sudden demand changes
- Discover seasonal sales behaviour
- Evaluate marketing campaigns
- Monitor inventory risk
- Improve operational decision making

---

# 🚀 Future Improvements

Future work may include:

- Machine Learning anomaly detection
  - Isolation Forest
  - Local Outlier Factor
  - Prophet

- Real-time dashboard

- Automatic email alerts

- Product-level forecasting

- Drill-down dashboard interaction

- Inventory optimization

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/gavinmay13/douyin-sales-monitor.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📸 Dashboard Preview

> *(Insert screenshots here after uploading dashboard images.)*

Example:

```
charts/dashboard_home.png
charts/dashboard_analysis.png
```

---

# 👨‍💻 Author

**Gavin Zhang**

