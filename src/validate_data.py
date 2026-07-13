"""
Validate feature data before anomaly detection.
"""

from load_data import load_feature_data


def validate_data(df):
    """
    Perform basic data validation.
    """

    print("=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)

    # Shape
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()

    # Missing values
    print("Missing Values:")
    print(df.isnull().sum())
    print()

    # Duplicate rows
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicate_count}")

    # Negative sales
    negative_sales = (df["daily_quantity"] < 0).sum()
    print(f"Negative Sales Rows: {negative_sales}")

    # Date range
    print(f"Earliest Date: {df['sales_date'].min()}")
    print(f"Latest Date: {df['sales_date'].max()}")

    print("=" * 50)


if __name__ == "__main__":

    df = load_feature_data()

    validate_data(df)

