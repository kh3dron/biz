import pandas as pd

class Backtest_Strategy():
    # This class should contain all the logic for a trading strategy to conduct a backtest. 
    # It will make assumptions about columns in the dataframe that is used with.

    def __init__():

        enteredLong = False
        enteredShort = False
        pass

    def LongEnter(self):
        if self.enteredShort or self.enteredLong:
            return False
        else:
            pass
        pass

    def LongProfit(self):
        if not self.enteredLong:
            return False
        else:
            pass

    def LongStopLoss(self):
        if not self.enteredLong:
            return False
        else:
            pass

    def LongTimeout(self):
        if not self.enteredLong:
            return False
        else:
            pass

    def ShortEnter(self):
        if self.enteredShort or self.enteredLong:
            return False
        else:
            pass

    def ShortProfit(self):
        if not self.enteredShort:
            return False
        else:
            pass

    def ShortStopLoss(self):
        if not self.enteredShort:
            return False
        else:
            pass

    def ShortTimeout(self):
        if not self.enteredShort:
            return False
        else:
            pass

    def Backtest(df):
        # This function accepts a df of historic stock data and an indicator logic object.
        # It will return a new dataframe of times when the indicator logic enters and exits long and short positions. 
        
        cols = ['Ticker', 'Date', 'Time', 'Action']
        results = pd.DataFrame(columns=cols)

        for row in df:
            pass
            


        return results