# Business Insights

## Sales Anomaly Dashboard

Author: Gavin Zhang

---

# Executive Summary

This project analyzes historical daily sales data to identify abnormal sales behaviour using a rule-based anomaly detection system.

A total of **24,287** sales records covering **660** products were analyzed. The dashboard automatically detects sales spikes, sales drops, and abnormal product behaviour, allowing business users to quickly identify operational issues and emerging opportunities.

The analysis provides valuable insights for inventory management, marketing evaluation, and business decision making.

---

# Business Overview

Dataset Summary

| Metric | Value |
|----------|---------|
| Total Records | 24,287 |
| Products | 660 |
| Total Sales | 115,479 |
| Sales Spike | 1,227 |
| Sales Drop | 1,718 |
| Zero Sales | 0 |

---

# Key Findings

## 1. Sales Drops Occur More Frequently Than Sales Spikes

The anomaly detection process identified:

- Sales Spike: **1,227**
- Sales Drop: **1,718**

Sales drops occur more frequently than sales spikes.

### Business Interpretation

This indicates that products are more likely to experience unexpected decreases in demand than sudden increases.

Possible reasons include:

- Inventory shortages
- Promotion ending
- Seasonal demand decline
- Competitor pricing
- Product lifecycle changes

Business teams should prioritize investigating abnormal sales drops because they may indicate operational risks.

---

## 2. Sales Behaviour Changes Across Different Months

Monthly anomaly analysis reveals that anomaly frequency changes over time rather than remaining constant.

Some months experience significantly more abnormal events.

### Business Interpretation

Possible causes include:

- Promotional campaigns
- Seasonal shopping behaviour
- Holiday effects
- Product launches
- Inventory replenishment

Monitoring monthly anomaly trends helps management evaluate business performance throughout the year.

---

## 3. A Small Number of Products Generate Most Abnormal Events

The Top Products dashboard shows that abnormal sales are concentrated within a relatively small group of products.

### Business Interpretation

These products deserve closer monitoring because they have the greatest impact on overall business performance.

Potential actions include:

- Inventory optimization
- Demand forecasting
- Marketing adjustment
- Supplier coordination

---

## 4. Continuous Sales Monitoring Improves Operational Efficiency

Without automated monitoring, analysts must manually review thousands of daily sales records.

The dashboard automatically identifies abnormal products, significantly reducing manual investigation time.

### Business Value

Business users can:

- Detect issues earlier
- Respond faster
- Reduce operational costs
- Improve reporting efficiency

---

# Operational Recommendations

Based on the detected anomalies, several operational improvements are recommended.

## Inventory Management

Products with repeated sales drops should be monitored for possible stock shortages.

Suggested actions:

- Increase inventory visibility
- Improve replenishment planning
- Monitor supplier performance

---

## Marketing Evaluation

Sales spikes often indicate successful promotional activities.

Suggested actions:

- Compare spikes with campaign schedules
- Measure promotion effectiveness
- Replicate successful marketing strategies

---

## Product Performance Monitoring

Products with frequent anomalies should receive additional attention.

Suggested actions:

- Weekly performance reviews
- Dynamic pricing analysis
- Product life-cycle monitoring

---

## Dashboard Deployment

The Streamlit dashboard can be used as a daily business monitoring tool.

Business users can quickly:

- Monitor KPI performance
- Detect abnormal products
- Review anomaly history
- Track sales trends

---

# Business Impact

The dashboard provides several measurable business benefits.

## Faster Decision Making

Managers can identify abnormal sales behaviour immediately rather than waiting for manual reports.

---

## Reduced Manual Analysis

Automated anomaly detection reduces repetitive data analysis tasks.

---

## Improved Inventory Planning

Sales drops provide early warning signals for inventory and supply chain issues.

---

## Better Marketing Evaluation

Sales spikes provide quantitative evidence for campaign performance.

---

## Increased Business Visibility

Interactive dashboards improve transparency across products and sales performance.

---

# Limitations

The current system uses a rule-based statistical approach.

Current limitations include:

- Fixed rolling window
- Threshold-based detection
- Historical data only
- No real-time monitoring
- No predictive anomaly detection

---

# Future Business Improvements

Future versions of this project may include:

- Machine Learning anomaly detection
- Real-time sales monitoring
- Automatic email alerts
- Forecast-driven anomaly prediction
- Inventory recommendation system
- Executive business reporting

---

# Conclusion

The Sales Anomaly Dashboard demonstrates how data engineering, statistical analysis, and interactive visualization can be combined to support business decision making.

Rather than relying on manual inspection, business users can quickly identify unusual sales behaviour, investigate abnormal products, and respond proactively to operational risks.

The dashboard provides a practical foundation for future business intelligence systems and can be extended with machine learning and real-time analytics as business needs evolve.
