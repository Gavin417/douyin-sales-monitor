# 📈 Sales Anomaly Dashboard

An interactive sales anomaly detection dashboard built with Python, Pandas, Plotly and Streamlit.

The project automatically detects abnormal sales behaviours from daily transaction data and provides an interactive dashboard for business monitoring.

---

## 🚀 Features

### 📊 Interactive Dashboard

- Daily Sales Trend
- Monthly Spike Analysis
- Monthly Drop Analysis
- Top Products Ranking
- Anomaly Details Table
- KPI Summary Cards

### 🔍 Interactive Filters

- Date Range Filter
- Product Search
- Anomaly Type Filter
- Top-N Product Slider

All charts and KPI metrics update dynamically based on user selections.

---

## 🚨 Supported Anomaly Types

- Sales Spike
- Sales Drop
- Zero Sales After Active
- Campaign Spike
- High Volatility

Each detected anomaly includes:

- Severity
- Reason
- Sales Date
- Product Name
- Daily Quantity

---

## 🛠 Tech Stack

- Python
- Pandas
- Plotly Express
- Streamlit
- PostgreSQL
- NumPy

---

## 📂 Project Structure

```
sales-anomaly-dashboard/
│
├── anomaly_detection/
│   ├── detect_spike.py
│   ├── detect_drop.py
│   ├── detect_zero_sales.py
│   ├── detect_campaign.py
│   ├── detect_volatility.py
│   └── run_detection.py
│
├── outputs/
│   ├── anomaly_report.csv
│   ├── dashboard_summary.csv
│   ├── dashboard_daily_sales.csv
│   ├── dashboard_top_products.csv
│   ├── campaign_spike.csv
│   └── high_volatility.csv
│
├── app.py
├── README.md
└── requirements.txt
```

---

## 📈 Dashboard Components

### KPI Cards

- Sales Spike Count
- Sales Drop Count
- Zero Sales Count
- Campaign Spike Count
- High Volatility Count

### Charts

- Daily Sales Trend
- Monthly Spike Count
- Monthly Drop Count
- Top Products by Sales

### Detail Table

The anomaly table contains:

- sales_date
- product_name
- anomaly_type
- severity
- reason
- daily_quantity

---

## ▶️ Run the Dashboard

Install dependencies

```bash
pip install -r requirements.txt
```

Run anomaly detection

```bash
python anomaly_detection/run_detection.py
```

Launch Streamlit

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Real-time anomaly monitoring
- Email alert system
- Database integration
- Forecasting model integration
- Interactive geographic visualization

---

## 👤 Author

Gavin Zhang

