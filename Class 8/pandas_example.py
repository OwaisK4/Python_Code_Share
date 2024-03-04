import pandas as pd

data = pd.read_csv("times.csv")

print(data.info())
print(data.shape)
print(data.head())
