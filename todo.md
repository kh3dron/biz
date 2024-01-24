- Smooth ingress of new data
  - not needed yet, only to be built out if I buy the big data stream
  - add standard suite of indicators at download time
  - do this on a cron schedule

- Master pipeline for designing backtests: 
  - Designing a strat: 
    - support for recursive logical indicator strats, like nested JSON access. AWS's cost explorer API had this implemented well, like so https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_cost_and_usage.html
  - a random name generator (like docker uses) would be excellent, so I don't have to deal with cramming detail into filenames 
  - Standard routines to analyze a backtest: 
    - computing alpha against range of benchmarks: 
      - sharpe ratio, max drawdown
      - alpha against index, alpha against underlying 

- Other ideas for things to try: 
  - random forrest combining many simple backtests / indicators