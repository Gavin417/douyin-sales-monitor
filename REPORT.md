# Sales Anomaly Dashboard Project Report

## Project Overview

The Sales Anomaly Dashboard is an interactive business analytics application designed to detect abnormal sales patterns and provide actionable insights through data visualization.

The project integrates anomaly detection algorithms with an interactive Streamlit dashboard, allowing users to monitor sales performance and investigate abnormal events efficiently.

---

## Objectives

The main objectives of this project are:

- Detect abnormal sales behaviours automatically.
- Help business users quickly identify unusual sales patterns.
- Provide clear explanations for detected anomalies.
- Support interactive exploration through an easy-to-use dashboard.

---

## Data Processing

The project processes daily sales data and performs:

- Data cleaning
- Data aggregation
- Daily sales calculation
- Dashboard summary generation

The processed datasets are then used for anomaly detection and visualization.

---

## Anomaly Detection Methods

Five anomaly detection methods were implemented.

### Sales Spike Detection

Detects products with unusually high sales compared with their historical average.

### Sales Drop Detection

Detects significant decreases in sales that may indicate operational or market issues.

### Zero Sales Detection

Identifies products that suddenly stop generating sales after previously being active.

### Campaign Spike Detection

Detects sales spikes likely caused by marketing campaigns or promotional activities.

### High Volatility Detection

Identifies products with unstable sales patterns requiring closer monitoring.

Each anomaly record includes:

- Severity Level
- Reason
- Product Name
- Sales Date
- Daily Quantity

---

## Dashboard Features

The Streamlit dashboard provides:

- KPI Summary Cards
- Daily Sales Trend
- Monthly Spike Analysis
- Monthly Drop Analysis
- Top Products Ranking
- Interactive Anomaly Table

Interactive filters include:

- Date Range Filter
- Product Search
- Anomaly Type Filter
- Top-N Product Selector

---

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly Express
- Streamlit
- PostgreSQL

---

## Results

The completed dashboard enables business users to:

- Detect abnormal sales quickly.
- Understand the severity of anomalies.
- Investigate abnormal products efficiently.
- Monitor sales performance interactively.

The project demonstrates how data analytics and visualization can support business decision-making.

---

## Future Improvements

Potential future work includes:

- Real-time anomaly monitoring
- Email alert system
- Machine learning based anomaly detection
- Sales forecasting integration
- Interactive geographic visualization
