import pandas as pd
import experiments.utils as utils
import matplotlib.pyplot as plt


source = 'TSLA_1min_firstratedata.csv'
df = pd.read_csv('data/' + source)

plt.plot(df['close'])
plt.show()