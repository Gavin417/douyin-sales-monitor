"""
Database configuration
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "douyin_ml",
    "user": "postgres",
    "password": "123123"
}

ANOMALY_CONFIG = {

    # Spike Detection
    "spike_threshold": 3.0,
    "min_sales": 5,

    # Drop Detection
    "drop_threshold": 0.3,

    # Zero Sales Detection
    "min_history_days": 7,

    # Severity Levels
    "high_severity": 5.0,
    "medium_severity": 3.0
}
