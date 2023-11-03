# let's try to predict the last hour of TSLA's price action

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the data
# columns: timestamp,open,high,low,close,volume,date,time
print("Loading data... ",)
df = pd.read_csv('data/cleaned_tsla.csv')
print("Loaded")

# PREPROCESSING
# delete any data with a time of 15:30:00 to 15:59:00, and all post-market data
df = df[~df['time'].between('00:01:00', '09:00:00')]
df = df[~df['time'].between('16:00:00', '23:59:00')]

df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour * 60 + pd.to_datetime(df['time'], format='%H:%M:%S').dt.minute
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'] = (df['date'] - df['date'].min()).dt.days + 1
df['datetime'] = df['date'] * 1440 + df['time']

df = df.drop(['timestamp'], axis=1)
df = df.drop(['date'], axis=1)
df = df.drop(['time'], axis=1)


print("Preprocessing Complete of ", len(df), "rows")
print(df.head())
    
# split into train and test sets, a random 80/20 split
df = df.sample(frac = 1)
train_size = int(0.8 * len(df))
train = df[:train_size]
test = df[train_size:]

# Model Selection
model = RandomForestRegressor()

# Train the model
print("Training model... ",)
model.fit(train.drop(['close'], axis=1), train['close'])
print("Trained")

# Test the model
print("Testing model... ",)
predictions = model.predict(test.drop(['close'], axis=1))
print("Tested")

# Calculate the error
print("Calculating error... ",)
mse = mean_squared_error(test['close'], predictions)
print("Error: ", mse)

# Plot the results
# x axis is each data point, y axis is the inaccuracy of the prediction
plt.plot(test['datetime'], test['close'] - predictions)
plt.xlabel('Time (minutes)')
plt.ylabel('Error (USD)')
plt.title('Error of Predictions')
plt.show()
