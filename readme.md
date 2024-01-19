# /biz/

Some notebooks for doing basic quant-y work with stock market data. 

Inspired by finding some free historic CSVs here: 
https://firstratedata.com/free-intraday-data

If you want to run these notebooks, you'll need to download these files and put them in the data/ directory implied by the file paths at the top of the notebooks. 

I don't have much of a background in statistics or finance, but I do feel pretty handy with these data science libraries. I'm more interested in datavis than trading or backtesting, so that's most of what this is. But if this repo goes private, know that I've struck gold. 


Some things I've done: 

- cross_file_correlation:
  - seaborne heatmap of correlation between tickers. VXX as the outlier that doesn't match the indexes and big tech. Makes sense. 
- rsi_backtesting:
  - Single indicator trades: enter at X, exit at Y, see how you would have performed over the last year. 
- indicator_stats:
  - Histogram chart of indicators forms a normal distributions - axiomatic for mean reversing indicators like RSI.
  - Overlayed RSI chart for all days of the past year on top of eachother. (This one is my favorite)
- option_investigating:
  - Chart the volatility surface in 3 dimensions in interactive plotly charts, fun to look around. 
  - Vol surface with volume is much harder to read