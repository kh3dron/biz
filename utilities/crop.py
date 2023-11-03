def market_hours_only(df):
    df = df.between_time('09:30', '16:00')
    return df