"""
Sales Drop Detection
"""

import os
import sys

# Allow importing modules from src/
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from config import ANOMALY_CONFIG
from load_data import load_feature_data

def assign_drop_severity(drop_ratio):
    if drop_ratio <= 0.10:
        return "High"
    elif drop_ratio <= 0.30:
        return "Medium"
    else:
        return "Low"

def detect_drop(df):
    """
    Detect sales drops based on the 7-day rolling average.

    Rule:
        rolling_mean_7 >= 5
        daily_quantity <= rolling_mean_7 * drop_threshold
    """

    drop_threshold = ANOMALY_CONFIG["drop_threshold"]

    data = df.copy()

    # Only evaluate SKUs that normally have meaningful sales
    data = data[
        data["rolling_mean_7"].notna()
        & (data["rolling_mean_7"] >= 5)
    ].copy()

    # Calculate how much of the normal sales level remains
    data["drop_ratio"] = (
        data["daily_quantity"]
        / data["rolling_mean_7"]
    )

    drop_df = data[
        data["drop_ratio"] <= drop_threshold
    ].copy()

    drop_df["anomaly_type"] = "SALES_DROP"
    
    drop_df["severity"] = drop_df["drop_ratio"].apply(assign_drop_severity)

    drop_df["reason"] = (
        "Sales dropped to "
        + (drop_df["drop_ratio"] * 100).round(1).astype(str)
        + "% of the 7-day average."
    )

    # More serious drops appear first
    drop_df = drop_df.sort_values(
        by="drop_ratio",
        ascending=True
    )

    return drop_df[
        [
            "sales_date",
            "sku_id",
            "product_name",
            "daily_quantity",
            "rolling_mean_7",
            "drop_ratio",
	    "severity",
	    "reason",
            "anomaly_type"
        ]
    ]


if __name__ == "__main__":

    df = load_feature_data()

    drop_df = detect_drop(df)

    print(drop_df.head())
    print()

    output_folder = "../outputs"
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(
        output_folder,
        "sales_drop.csv"
    )

    drop_df.to_csv(
        output_path,
        index=False
    )

    print(f"Saved to: {output_path}")
    print(f"Drop Count: {len(drop_df)}")
