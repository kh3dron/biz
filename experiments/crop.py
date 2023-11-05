def time_crop(df, fields):
    if "market_hours" in fields:
        df = market_hours_only(df)
    return df

def market_hours_only(df):
    df = df.between_time('09:30', '16:00')
    return df

