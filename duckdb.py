import duckdb
import glob

duckdb.read_csv('data/stocks/AAPL_full_1min_adjsplit.txt.csv')

duckdb.sql('SELECT * FROM data/stocks/AAPL_full_1min_adjsplit.txt.csv')