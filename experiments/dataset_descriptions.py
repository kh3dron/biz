import pandas as pd

# Split timestamps into date and time
def timestamp_to_date_and_time(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')    
    return df
