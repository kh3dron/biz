import pandas as pd

def add_indicators(df, fields):
    if "RSI_14" in fields:
        df = RSI(df, 14)
    if "EMA_50" in fields:
        df = EMA(df, 50)
    return df

def RSI(df, n):
    fieldName = "RSI_" + str(n)
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
    df[fieldName] = RSI.round(4)
    return df

def EMA(df, n):
    fieldName = "EMA_" + str(n)
    EMA = pd.Series(df['close'].ewm(span=n, min_periods=n).mean(), name=fieldName)
    df = df.join(EMA)
    return df