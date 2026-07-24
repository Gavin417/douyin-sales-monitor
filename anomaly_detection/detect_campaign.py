"""
Campaign Spike Detection
"""

import os
import sys

import pandas as pd

# Allow importing from src/
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from load_data import load_feature_data
from config import ANOMALY_CONFIG

def assign_spike_severity(spike_ratio):
    if spike_ratio >= 5:
        return "High"
    elif spike_ratio >= 3:
        return "Medium"
    else:
        return "Low"

def detect_campaign(df):

    spike_threshold = ANOMALY_CONFIG["spike_threshold"]
    min_sales = ANOMALY_CONFIG["min_sales"]

    data = df.copy()

    # 避免除以 0
    data = data[data["rolling_mean_7"] > 0]

    data["spike_ratio"] = (
        data["daily_quantity"]
        / data["rolling_mean_7"]
    )

    campaign_df = data[
    (data["daily_quantity"] >= min_sales)
    &
    (data["spike_ratio"] >= spike_threshold)
    &
    (
        (data["is_618"] == 1)
        |
        (data["is_double11"] == 1)
        |
        (data["is_double12"] == 1)
        |
        (data["is_public_holiday"] == 1)
    )
].copy()

    campaign_df["anomaly_type"] = "CAMPAIGN_SPIKE"
    
    campaign_df["severity"] = campaign_df["spike_ratio"].apply(assign_spike_severity)
    
    campaign_df["reason"] = (
    "Campaign-driven sales spike: Sales are "
    + campaign_df["spike_ratio"].round(2).astype(str)
    + "x higher than the 7-day average."
)

    return campaign_df[
        [
            "sales_date",
            "sku_id",
            "product_name",
            "daily_quantity",
            "rolling_mean_7",
            "spike_ratio",
	    "severity",
	    "reason",
            "anomaly_type"
        ]
    ]


if __name__ == "__main__":

    df = load_feature_data()

    campaign_df = detect_campaign(df)

    # 显示前5条异常
    print(campaign_df.head())
    print()

    # 创建 outputs 文件夹（如果不存在）
    output_folder = "../outputs"
    os.makedirs(output_folder, exist_ok=True)

    # 保存结果
    output_path = os.path.join(
        output_folder,
        "campaign_spike.csv"
    )

    campaign_df.to_csv( 
        output_path,
        index=False
    )

    print(f"Saved to: {output_path}")
    print(f"Campaign Spike Count: {len(campaign_df)}")
