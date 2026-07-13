"""
Sales Spike Detection
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


def detect_spike(df):

    spike_threshold = ANOMALY_CONFIG["spike_threshold"]
    min_sales = ANOMALY_CONFIG["min_sales"]

    data = df.copy()

    # 避免除以 0
    data = data[data["rolling_mean_7"] > 0]

    data["spike_ratio"] = (
        data["daily_quantity"]
        / data["rolling_mean_7"]
    )

    spike_df = data[
        (data["daily_quantity"] >= min_sales)
        &
        (data["spike_ratio"] >= spike_threshold)
    ].copy()

    spike_df["anomaly_type"] = "SALES_SPIKE"

    return spike_df[
        [
            "sales_date",
            "sku_id",
            "product_name",
            "daily_quantity",
            "rolling_mean_7",
            "spike_ratio",
            "anomaly_type"
        ]
    ]


if __name__ == "__main__":

    df = load_feature_data()

    spike_df = detect_spike(df)

    # 显示前5条异常
    print(spike_df.head())
    print()

    # 创建 outputs 文件夹（如果不存在）
    output_folder = "../outputs"
    os.makedirs(output_folder, exist_ok=True)

    # 保存结果
    output_path = os.path.join(
        output_folder,
        "sales_spike.csv"
    )

    spike_df.to_csv(
        output_path,
        index=False
    )

    print(f"Saved to: {output_path}")
    print(f"Spike Count: {len(spike_df)}")
