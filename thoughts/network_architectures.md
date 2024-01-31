Observations
- Not equipped for HFT or arb. 1 Day charts feel like the best bet for my data stream
- Should be straightforward to use last ~1-3 months of data for testing. should know quickly if anything has potential

Things to represent in data: 
- What's the best thing to "predict"?
  - Could normalize price data from -1 to 1, best time to buy / sell on a given day. 
    - That would mean no way to differentiate between a +.1% day and a +5% day. 
    - Could modify this window - best or worst time to by in the last week, last 100 candles, etc
- Model architecture
  - RNN / transformer feels right since data is sequential, NN seems incorrect
- Indicators v. hidden layers
  - most indicators are just calculated off of moving averages, etc. 
  - Hidden layers should construct similar features on their own in a NN. will be interesting to observe
- How to weigh importance of tickers in training data
  - normalize by volume over all tickers? AAPL's behavior should be matter more than some random tiny co
  - Or perhaps not? who knows 


something to try right away:
- Add as many indicators as possible and normalize
- RNN
- ???
- profit