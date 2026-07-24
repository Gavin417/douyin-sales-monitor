"""
Load feature data from PostgreSQL
"""

import pandas as pd

from db import get_connection
from db import close_connection


def load_feature_data():

    conn = get_connection()

    query = """
    SELECT *
    FROM forecast_features_v2;
    """

    df = pd.read_sql(query, conn)

    close_connection(conn)

    return df


if __name__ == "__main__":

    df = load_feature_data()

    print(df.head())

    print()

    print(df.shape)

    print(df.columns.tolist())
    
    print(df["rolling_std_7"].describe())
