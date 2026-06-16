import pandas as pd

def engineer_features(df):
    df = df.copy()
    
    df["watch_ratio"] = df["watch_time"] / df["content_duration"]
    df["rewatch_rate"] = df["rewatches"] / (df["session_length"] + 1)
    df["skip_rate"] = df["skips"] / (df["session_length"] + 1)
    df["is_prime_time"] = df["time_of_day"].between(18, 23).astype(int)
    df["engagement_signal"] = df["watch_ratio"] * (1 + df["rewatches"]) - (df["skips"] * 0.2)

    return df

def get_feature_columns():
    return [
        "watch_ratio",
        "rewatch_rate",
        "skip_rate",
        "is_prime_time",
        "engagement_signal",
        "session_length",
        "time_of_day"
    ]