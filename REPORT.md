# Sales Anomaly Dashboard
## Project Report

**Author:** Gavin Zhang

**Project Type:** Data Analytics / Business Intelligence

**Programming Language:** Python

**Database:** PostgreSQL

**Visualization:** Streamlit + Plotly

---

# 1. Introduction

Retail companies generate thousands of sales transactions every day across hundreds of products. Monitoring these sales manually is inefficient and makes it difficult to identify unusual business events in time.

This project develops an automated sales anomaly detection system that continuously monitors daily product sales, detects abnormal sales patterns, and visualizes the results through an interactive Streamlit dashboard.

The project combines data engineering, statistical anomaly detection, and business intelligence techniques to provide an end-to-end monitoring solution.

---

# 2. Project Objectives

The primary objectives of this project are:

- Build a complete sales monitoring pipeline
- Store and manage sales data using PostgreSQL
- Validate data quality before analysis
- Detect abnormal sales behaviour automatically
- Generate dashboard-ready datasets
- Develop an interactive dashboard for business users

The final system enables users to quickly identify unusual sales activities and support operational decision making.

---

# 3. Dataset

The project uses historical daily product sales data.

Dataset Summary

| Metric | Value |
|----------|---------|
| Total Records | 24,287 |
| Products | 660 |
| Total Sales | 115,479 |
| Time Period | Dec 2024 – Jan 2026 |

Each record contains:

- Sales Date
- Product Name
- SKU ID
- Daily Sales Quantity

---

# 4. System Architecture

The complete workflow is shown below.

```
Daily Sales Data
        │
        ▼
 PostgreSQL Database
        │
        ▼
 Data Loading
        │
        ▼
 Data Validation
        │
        ▼
 Rolling Statistics
        │
        ▼
 Spike / Drop Detection
        │
        ▼
 Dashboard Dataset
        │
        ▼
 Streamlit Dashboard
```

---

# 5. Data Engineering

The first stage focuses on building a reliable data pipeline.

Completed tasks include:

- PostgreSQL database creation
- Python database connection using psycopg2
- SQL data extraction
- Data loading into Pandas
- Dashboard dataset generation

This ensures that the dashboard always uses validated and structured data.

---

# 6. Data Validation

Before anomaly detection, several data quality checks are performed.

Validation includes:

- Missing value detection
- Duplicate row detection
- Negative sales detection
- Date range verification

Validation Results

- Duplicate Rows: 0
- Negative Sales: 0

The dataset passed all validation checks and was considered suitable for anomaly detection.

---

# 7. Feature Engineering

Feature engineering prepares the dataset for statistical analysis.

The following features are generated:

- Daily Sales
- Rolling Mean (7-day window)
- Spike Ratio
- Drop Ratio

Rolling statistics are calculated independently for each product.

---

# 8. Anomaly Detection Method

This project adopts a rule-based anomaly detection approach.

For each product:

1. Calculate a rolling average using the previous seven days.
2. Compare current daily sales with the rolling average.
3. Classify anomalies.

Three anomaly types are detected.

## Sales Spike

Sales are significantly higher than the rolling average.

Example

Rolling Mean = 20

Current Sales = 80

Spike Ratio = 4.0

The record is classified as a sales spike.

---

## Sales Drop

Sales are significantly lower than the rolling average.

Example

Rolling Mean = 40

Current Sales = 4

Drop Ratio = 0.10

The record is classified as a sales drop.

---

## Zero Sales

Products with zero sales after active selling periods are identified separately.

---

# 9. Dashboard Design

An interactive dashboard was developed using Streamlit and Plotly.

The dashboard consists of several business modules.

## KPI Summary

Displays:

- Total Records
- Products
- Average Daily Sales
- Total Sales

---

## Daily Sales Trend

Interactive line chart displaying long-term sales behaviour.

Users can observe:

- Growth trends
- Seasonal fluctuations
- Overall sales performance

---

## Monthly Spike Analysis

Displays monthly spike counts.

Business users can identify periods with unusually high sales activity.

---

## Monthly Drop Analysis

Displays monthly drop counts.

Useful for monitoring inventory risks and product performance.

---

## Top Products

Displays the highest-selling products using a horizontal ranking chart.

---

## Anomaly Detail Table

Displays detailed anomaly records including:

- Date
- Product Name
- Anomaly Type
- Ratio

This enables users to investigate abnormal products efficiently.

---

# 10. Project Results

The anomaly detection pipeline successfully identified abnormal sales events.

Detection Summary

| Type | Count |
|--------|---------|
| Sales Spike | 1,227 |
| Sales Drop | 1,718 |
| Zero Sales | 0 |

These anomalies are automatically visualized within the dashboard.

---

# 11. Business Value

The dashboard provides several practical business benefits.

### Sales Monitoring

Automatically monitors daily sales behaviour.

### Marketing Evaluation

Measures the effectiveness of promotions through spike analysis.

### Inventory Management

Identifies products experiencing unexpected demand changes.

### Decision Support

Provides managers with clear business insights through interactive visualizations.

---

# 12. Limitations

Although the project performs well, several limitations remain.

Current limitations include:

- Rule-based anomaly detection only
- Fixed rolling window size
- No real-time data streaming
- No automatic notification system

These areas provide opportunities for future improvement.

---

# 13. Future Improvements

Potential future work includes:

- Isolation Forest anomaly detection
- Local Outlier Factor (LOF)
- Prophet time-series anomaly detection
- Real-time dashboard updates
- Email alert system
- Product-level forecasting
- Inventory optimization
- Interactive drill-down dashboard

---

# 14. Conclusion

This project demonstrates a complete end-to-end business analytics workflow.

Starting from raw sales data stored in PostgreSQL, the system performs data validation, statistical anomaly detection, dashboard dataset generation, and interactive visualization using Streamlit.

The final dashboard enables users to monitor product performance efficiently while supporting business decision making through automated anomaly detection.

Overall, this project demonstrates practical skills in:

- Data Engineering
- SQL
- PostgreSQL
- Python
- Statistical Analysis
- Business Intelligence
- Dashboard Development
- Data Visualization
- Git & GitHub
