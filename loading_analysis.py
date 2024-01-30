# load all the txt files in data/ into a list of dataframes

import pandas as pd
import os

indexes_path = "data/index_full_1min_n1q56ok/"


def load_data(path, limit_read = 5):
    data = []
    for filename in os.listdir(path):
        if limit_read == 0:
            return data
        limit_read -= 1
        if filename.endswith(".txt"):
            df = pd.read_csv(path + filename)
            # remove tjhe file extension from the date
            ticker = filename.replace("_full_1min.txt", "")
            print(ticker)

            df["ticker"] = ticker
            data.append(df)

    return data

# load the data into a list of dataframes
data = load_data(indexes_path)

print("Loaded", len(data), "tickers")