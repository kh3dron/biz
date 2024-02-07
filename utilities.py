# Methods to read in CSVs, clean data, and add indicators.

import pandas as pd
import datetime
import os

### DATA LOADING
# These directories might have different structures for index/futures/stocks, so each gets their own loading function. 

def load_indexes(limit_read = -1):
    path = "../data/index_full_1min_n1q56ok/"
    data = []
    for filename in os.listdir(path):
        if limit_read == 0:
            return data
        limit_read -= 1
        if filename.endswith(".txt"):
            df = pd.read_csv(path + filename)
            df.columns = ["timestamp", "open", "high", "low", "close"]

            ticker = filename.replace("_full_1min.txt", "")
            df["ticker"] = ticker

            df = timestamp_to_date_and_time(df)
            data.append(df)

    return data

def load_index(ticker):
    df = pd.read_csv(f'../data/etfs/{ticker}_full_1min_adjsplit.txt')
    df.columns = ["timestamp", "open", "high", "low", "close", 'volume']
    df["ticker"] = ticker
    df = timestamp_to_date_and_time(df)
    return df

def load_stock(ticker):
    df = pd.read_csv(f'../data/stocks/{ticker}_full_1min_adjsplit.txt')
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
    df["ticker"] = ticker
    df = timestamp_to_date_and_time(df)
    df = time_to_numeric(df)

    return df

### TIME

def timestamp_to_date_and_time(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    return df

def market_hours_only(df):
    df = df[(df["time"] >= datetime.time(9, 30)) & (df["time"] <= datetime.time(16, 0))]
    return df

def option_hours_only(df):
    df = df[(df["time"] >= datetime.time(9, 30)) & (df["time"] <= datetime.time(16, 0))]
    return df

def count_days(df):
    df['date'] = df['timestamp'].dt.date
    return len(df["date"].unique())

def list_of_day_dfs(df):
    days = []
    for day in df["date"].unique():
        days.append(df[df["date"] == day])
    return days

def time_to_numeric(df):
    df["minute"] = df["time"].apply(lambda x: x.hour*60 + x.minute)
    return df

### DATA SANITIZING

#TODO: rewrite this, just moving this here to delete files
def missing_minutes(df):

    max_gap_minutes = 240

    missing_minutes = 0
    gaps = []
    # Sort DataFrame by timestamp
    df = df.sort_values(by='timestamp')

    # Iterate through timestamps to find missing minutes
    for i in range(1, len(df)):
        time_diff = (df['timestamp'].iloc[i] - df['timestamp'].iloc[i - 1]).total_seconds() / 60  # Convert to minutes
        if time_diff > 1 and time_diff <= max_gap_minutes:
            missing_minutes += int(time_diff) - 1
            gaps.append(int(time_diff) - 1)

    print("Number of missing minutes:", missing_minutes, "out of", len(df), "total minutes", "(" + str(round(missing_minutes / len(df) * 100, 2)) + "%)")

def missing_markethours(df):
    df = market_hours_only(df)
    return 1-(len(df) / (len(df["date"].unique()) * 390))

### DATA RESHAPING

def compress_candles(df, minutes):
    new_frame = pd.DataFrame(columns=df.columns)
    lines = len(df)
    
    for e in range(0, lines, minutes):
        data_slice = df.iloc[e:e+minutes]
        print(data_slice)
        open = data_slice['open'].iloc[0]
        high = data_slice['high'].max()
        low = data_slice['low'].min()
        close = data_slice['close'].iloc[-1]
        volume = data_slice['volume'].sum()
        date = data_slice['date'].iloc[0]
        time = data_slice['time'].iloc[0]
        
        new_frame.loc[len(new_frame)] = {'open': open, 'high': high, 'low': low, 'close': close, 'volume': volume, 'date': date, 'time': time}

    return new_frame

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
    df["rsi" + str(n)] = RSI.round(4)
    df = df.drop(columns=["up", "down"])
    return df

def MACD(df, n_fast=12, n_slow=26, n_signal=9):
    EMAfast = df["close"].ewm(span=n_fast, min_periods=n_slow).mean()
    EMAslow = df["close"].ewm(span=n_slow, min_periods=n_slow).mean()
    MACD = EMAfast - EMAslow
    df["macd"] = MACD.round(4)
    signal = MACD.ewm(span=n_signal, min_periods=n_signal).mean()
    df["signal"] = signal.round(4)
    df["histogram"] = (MACD - signal).round(4)
    return df

def EMA(df, n):
    EMA = df["close"].ewm(span=n, min_periods=n).mean()
    df["ema" + str(n)] = EMA.round(4)
    return df