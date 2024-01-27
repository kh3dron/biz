import pandas as pd

class Backtest_Strategy():
    # This class should contain all the logic for a trading strategy to conduct a backtest. 
    # It will make assumptions about columns in the dataframe that is used with.

    def __init__(self):

        self.entryTime = None
        self.enteredLong = False

    def LongEnter(self, row):
        if not self.enteredLong and row["RSI14"] < 50:
            self.enteredLong = True
            self.entryTime = row["Time"]
            return True

    def LongProfit(self, row):
        if self.enteredLong and row["RSI14"] > 70:
            self.enteredLong = False
            return True

    def LongStopLoss(self, row):
        if self.enteredLong and row["RSI14"] < 50:
            self.enteredLong = False
            return True

    def LongTimeout(self, row):
        if self.enteredLong and self.entryTime + 60 < row["Time"]:
            self.enteredLong = False
            return True

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
                results = pd.concat([results, pd.DataFrame([[row["Ticker"], row["Date"], row["Time"], action]], columns=cols)])

        return results
    

testing = Backtest_Strategy()