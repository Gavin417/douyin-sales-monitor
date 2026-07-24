"""
High Volatility Detection
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

def assign_volatility_severity(volatility):
    if volatility >= 30:
        return "High"
    elif volatility >= 20:
        return "Medium"
    else:
        return "Low"

def detect_volatility(df):

    volatility_threshold = 10

    data = df.copy()

    volatility_df = data[
    data["rolling_std_7"] >= volatility_threshold
].copy()

    volatility_df["anomaly_type"] = "HIGH_VOLATILITY"
    
    volatility_df["severity"] = (
    volatility_df["rolling_std_7"]
    .apply(assign_volatility_severity)
)
    
    volatility_df["reason"] = (
    "High sales volatility: 7-day rolling standard deviation = "
    + volatility_df["rolling_std_7"].round(2).astype(str)
)

    return volatility_df[
    [
        "sales_date",
        "sku_id",
        "product_name",
        "daily_quantity",
        "rolling_std_7",
        "severity",
        "reason",
        "anomaly_type",
    ]
]

if __name__ == "__main__":

    df = load_feature_data()

    volatility_df = detect_volatility(df)

    # 显示前5条异常
    print(volatility_df.head())
    print()

    # 创建 outputs 文件夹（如果不存在）
    output_folder = "../outputs"
    os.makedirs(output_folder, exist_ok=True)

    # 保存结果
    output_path = os.path.join(
    output_folder,
    "high_volatility.csv"
)

    volatility_df.to_csv(
    output_path,
    index=False
)

    print(f"Saved to: {output_path}")
    print(f"High Volatility Count: {len(volatility_df)}")
