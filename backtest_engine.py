import pandas as pd

class Backtest_Strategy():
    # This class should contain all the logic for a trading strategy to conduct a backtest. 
    # It will make assumptions about columns in the dataframe that is used with.

    def __init__(self):

        self.enteredLong = False
        self.enteredShort = False

        self.entryTime = None

    def LongEnter(self, row):
        return not (self.enteredLong or self.enteredShort) and row["RSI14"] < 50

    def LongProfit(self, row):
        return self.enteredLong and row["RSI14"] > 70

    def LongStopLoss(self, row):
        return self.enteredLong and row["RSI14"] < 50

    def LongTimeout(self, row):
        return self.enteredLong and self.entryTime + 60 < row["Time"]

    def Backtest(self, df):
        # This function accepts a df of historic stock data and an indicator logic object.
        # It will return a new dataframe of times when the indicator logic enters and exits long and short positions. 
        
        cols = ['Ticker', 'Date', 'Time', 'Action']
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
                results = results.append(row[cols].to_dict(), ignore_index=True)

        return results