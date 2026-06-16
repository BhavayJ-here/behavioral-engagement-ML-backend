import pandas as pd
import numpy as np
import os

np.random.seed(42)

CONTENT_IDS = [f"vid_{i}" for i in range(1, 21)]
N_SESSIONS = 1000

def generate_sessions():
    users = np.random.randint(1, 51, N_SESSIONS)
    content = np.random.choice(CONTENT_IDS, N_SESSIONS)
    watch_time = np.random.randint(10, 600, N_SESSIONS)
    duration = np.random.randint(60, 600, N_SESSIONS)
    skips = np.random.randint(0, 5, N_SESSIONS)
    rewatches = np.random.randint(0, 3, N_SESSIONS)
    time_of_day = np.random.randint(0, 24, N_SESSIONS)
    session_length = np.random.randint(1, 10, N_SESSIONS)

    watch_ratio = watch_time / duration
    engaged = ((watch_ratio > 0.6) & (skips < 2)).astype(int)

    df = pd.DataFrame({
        "session_id": range(N_SESSIONS),
        "user_id": users,
        "content_id": content,
        "watch_time": watch_time,
        "content_duration": duration,
        "skips": skips,
        "rewatches": rewatches,
        "time_of_day": time_of_day,
        "session_length": session_length,
        "engaged": engaged
    })

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sessions.csv", index=False)
    print(f"Generated {N_SESSIONS} sessions -> data/sessions.csv")
    print(df.head())

if __name__ == "__main__":
    generate_sessions()