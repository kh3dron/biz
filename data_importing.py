# Methods to read in CSVs, clean data, and add indicators.

import pandas as pd
import datetime

### TIME

def timestamp_to_date_and_time(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')
    return df

def market_hours_only(df):
    df = df[(df["time"] >= datetime.time(9, 00)) & (df["time"] <= datetime.time(16, 0))]
    return df

def option_hours_only(df):
    df = df[(df["time"] >= datetime.time(9, 30)) & (df["time"] <= datetime.time(16, 0))]
    return df

### INDICATORS

def RSI(df, n):
    "function to calculate RSI"
    delta = df["close"].diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    df["up"] = up.round(4)
    df["down"] = down.round(4)
    AVG_Gain = df["up"].rolling(window=n).mean()
    AVG_Loss = abs(df["down"].rolling(window=n).mean())
    RS = AVG_Gain / AVG_Loss
    RSI = 100.0 - (100.0 / (1.0 + RS))
    df["RSI_14"] = RSI.round(4)
    df = df.drop(columns=["up", "down"])

    return df