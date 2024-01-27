import pandas as pd
import datetime

from data_importing import *

class Backtest():
    # This class should contain all the logic for a trading strategy to conduct a backtest. 
    # It will make assumptions about columns in the dataframe that is used with.

    def __init__(self):

        self.entryTime = None
        self.enteredLong = False

    def LongEnter(self, row):
        if not self.enteredLong and row["rsi14"] < 50:
            self.enteredLong = True
            self.entryTime = row["time"]
            return True
        return False

    def LongProfit(self, row):
        if self.enteredLong and row["rsi14"] > 70:
            self.enteredLong = False
            return True
        return False

    def LongStopLoss(self, row):
        if self.enteredLong and row["rsi14"] < 50:
            self.enteredLong = False
            return True
        return False

    def LongTimeout(self, row):
        if self.enteredLong:
            if row["time"] > self.entryTime + datetime.timedelta(minutes=30) or row["time"] >= datetime.time(16, 00):
                self.enteredLong = False
                return True
        return False

    def test(self, df):
        # This function accepts a df of historic stock data and an indicator logic object.
        # It will return a new dataframe of times when the indicator logic enters and exits long and short positions. 
        
        cols = ['ticker', 'date', 'time', 'action']
        results = pd.DataFrame(columns=cols)

        for index, row in df.iterrows():
            action = None
            if self.LongEnter(row):
                action = "LongEnter"
            elif self.LongProfit(row):
                action = "LongProfit"
            elif self.LongStopLoss(row):
                action = "LongStopLoss"
            elif self.LongTimeout(row):
                action = "LongTimeout"

            if action is not None:
                results = pd.concat([results, pd.DataFrame([[row["ticker"], row["date"], row["time"], action]], columns=cols)])

        return results

df = pd.read_csv("data/SPY_1min_firstratedata.csv")
df["ticker"] = "SPY"

df = timestamp_to_date_and_time(df)
df = RSI(df, 14)
df = market_hours_only(df)

testing = Backtest()
results = testing.test(df)
results.to_csv("results.csv", index=False)