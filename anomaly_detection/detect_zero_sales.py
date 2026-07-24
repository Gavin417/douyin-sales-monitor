"""
Zero Sales After Active Sales Detection
"""

import os
import sys

# Allow importing modules from src/
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from load_data import load_feature_data

def assign_zero_sales_severity(rolling_mean):
    if rolling_mean >= 20:
        return "High"
    elif rolling_mean >= 10:
        return "Medium"
    else:
        return "Low"

def detect_zero_sales(df):
    """
    Detect SKUs that suddenly have zero sales after active sales.

    Rule:
        daily_quantity == 0
        rolling_mean_7 >= 3
    """

    data = df.copy()

    zero_sales_df = data[
        data["rolling_mean_7"].notna()
        & (data["daily_quantity"] == 0)
        & (data["rolling_mean_7"] >= 3)
    ].copy()

    zero_sales_df["anomaly_type"] = "ZERO_SALES_AFTER_ACTIVE"
    
    zero_sales_df["severity"] = (
        zero_sales_df["rolling_mean_7"]
        .apply(assign_zero_sales_severity)
    )

    zero_sales_df["reason"] = (
        "Sales dropped to zero after averaging "
        + zero_sales_df["rolling_mean_7"].round(1).astype(str)
        + " units/day over the past 7 days."
    )

    zero_sales_df = zero_sales_df.sort_values(
        by="rolling_mean_7",
        ascending=False
    )

    return zero_sales_df[
        [
            "sales_date",
            "sku_id",
            "product_name",
            "daily_quantity",
            "rolling_mean_7",
            "severity",
            "reason",
            "anomaly_type"
        ]
    ]


if __name__ == "__main__":

    df = load_feature_data()

    zero_sales_df = detect_zero_sales(df)

    print(zero_sales_df.head())
    print()

    output_folder = "../outputs"
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(
        output_folder,
        "zero_sales_after_active.csv"
    )

    zero_sales_df.to_csv(
        output_path,
        index=False
    )

    print(f"Saved to: {output_path}")
    print(f"Zero Sales Count: {len(zero_sales_df)}")

