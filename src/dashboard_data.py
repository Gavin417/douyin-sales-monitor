"""
Prepare dashboard summary data.
"""

import os
import pandas as pd

from load_data import load_feature_data


def build_dashboard_summary(df):

    import os
    import pandas as pd

    spike_count = 0
    drop_count = 0
    zero_count = 0

    if os.path.exists("outputs/sales_spike.csv"):
        spike_count = len(pd.read_csv("outputs/sales_spike.csv"))

    if os.path.exists("outputs/sales_drop.csv"):
        drop_count = len(pd.read_csv("outputs/sales_drop.csv"))

    if os.path.exists("outputs/zero_sales_after_active.csv"):
        zero_count = len(pd.read_csv("outputs/zero_sales_after_active.csv"))

    summary = pd.DataFrame({
        "total_records":[len(df)],
        "total_products":[df["product_id"].nunique()],
        "avg_daily_sales":[df["daily_quantity"].mean()],
        "total_sales":[df["daily_quantity"].sum()],
        "total_spike":[spike_count],
        "total_drop":[drop_count],
        "total_zero":[zero_count]
    })

    return summary

def build_daily_sales(df):

    daily = (
        df.groupby("sales_date")["daily_quantity"]
        .sum()
        .reset_index()
        .sort_values("sales_date")
    )

    return daily


def build_top_products(df):

    top_products = (
        df.groupby("product_name")["daily_quantity"]
        .sum()
        .reset_index()
        .sort_values(
            "daily_quantity",
            ascending=False
        )
        .head(20)
    )

    return top_products


def main():

    df = load_feature_data()

    output_folder = "outputs"

    os.makedirs(output_folder, exist_ok=True)

    summary = build_dashboard_summary(df)
    daily = build_daily_sales(df)
    top = build_top_products(df)

    summary.to_csv(
        os.path.join(output_folder, "dashboard_summary.csv"),
        index=False
    )

    daily.to_csv(
        os.path.join(output_folder, "dashboard_daily_sales.csv"),
        index=False
    )

    top.to_csv(
        os.path.join(output_folder, "dashboard_top_products.csv"),
        index=False
    )

    print("=" * 50)
    print("Dashboard files generated")
    print("=" * 50)

    print(f"Summary rows : {len(summary)}")
    print(f"Daily rows   : {len(daily)}")
    print(f"Top products : {len(top)}")


if __name__ == "__main__":
    main()
