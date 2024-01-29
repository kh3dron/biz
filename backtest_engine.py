import pandas as pd
import datetime
from data_importing import *

class Backtest():
    MAX_DAILY_TRADES = 1
    RSI_OVERSOLD_THRESHOLD = 50
    RSI_OVERBOUGHT_THRESHOLD = 70
    RSI_STOP_LOSS_THRESHOLD = 40
    TIMEOUT_EXIT = datetime.time(15, 59)  # Market closing time - 1 minute

    def __init__(self):
        self.entry_time = None
        self.entered_long = False

    def execute_action(self, row):
        action = None

        if not self.entered_long and row["rsi14"] < self.RSI_OVERSOLD_THRESHOLD:
            self.entered_long = True
            self.entry_time = row["time"]
            action = "LongEnter"

        elif self.entered_long and row["rsi14"] > self.RSI_OVERBOUGHT_THRESHOLD:
            self.entered_long = False
            action = "LongProfit"

        elif self.entered_long and row["rsi14"] < self.RSI_STOP_LOSS_THRESHOLD:
            self.entered_long = False
            action = "LongStopLoss"

        elif self.entered_long and (row["time"] == self.TIMEOUT_EXIT):
            self.entered_long = False
            action = "LongTimeout"

        return action

    def test(self, df):
        cols = ['ticker', 'date', 'time', 'action']
        results = []

        days = list_of_day_dfs(df)
        for day in days:
            executed_trades = 0

            for index, row in day.iterrows():
                if executed_trades >= self.MAX_DAILY_TRADES:
                    break

                action = self.execute_action(row)

                if action:
                    results.append([row["ticker"], row["date"], row["time"], action])
                    executed_trades += 1

        return pd.DataFrame(results, columns=cols)

df = pd.read_csv("data/SPY_1min_firstratedata.csv")
df["ticker"] = "SPY"
df = timestamp_to_date_and_time(df)
df = RSI(df, 14)
df = market_hours_only(df)

testing = Backtest()
results = testing.test(df)
results.to_csv("results.csv", index=False)
