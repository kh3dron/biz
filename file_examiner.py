import os
import re

tickers = []

def list_files_and_extract_ticker(directory):

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)            
            ticker = file.split("_")[0]
            tickers.append(ticker)

directory_path = "data"
list_files_and_extract_ticker(directory_path)

print("found", len(tickers), "tickers")