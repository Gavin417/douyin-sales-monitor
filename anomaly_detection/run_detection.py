"""
Merge all anomaly detection results.
"""

import os
import pandas as pd


def load_csv(file_path):
    """
    Load a CSV if it exists.
    Return an empty DataFrame otherwise.
    """

    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    return pd.DataFrame()


def main():

    output_folder = "../outputs"

    spike = load_csv(
        os.path.join(output_folder, "sales_spike.csv")
    )

    drop = load_csv(
        os.path.join(output_folder, "sales_drop.csv")
    )

    zero = load_csv(
        os.path.join(output_folder, "zero_sales_after_active.csv")
    )
    
    campaign = load_csv(
        os.path.join(output_folder, "campaign_spike.csv")
    )
    
    volatility = load_csv(
        os.path.join(output_folder, "high_volatility.csv")
    )

    anomaly_report = pd.concat(
        [
            spike,
            drop,
            zero,
            campaign,
            volatility
        ],
        ignore_index=True
    )

    anomaly_report.to_csv(
        os.path.join(
            output_folder,
            "anomaly_report.csv"
        ),
        index=False
    )

    print("=" * 50)
    print("ANOMALY SUMMARY")
    print("=" * 50)

    print(f"Spike Records : {len(spike)}")
    print(f"Drop Records  : {len(drop)}")
    print(f"Zero Records  : {len(zero)}")
    print(f"Campaign Records : {len(campaign)}")
    print(f"High Volatility Records : {len(volatility)}")

    print("-" * 50)

    print(f"Total Records : {len(anomaly_report)}")

    print()

    print("Saved to:")
    print("../outputs/anomaly_report.csv")


if __name__ == "__main__":
    main()
