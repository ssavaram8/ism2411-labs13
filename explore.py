# Self Assessment Questions:
# 1.

#2. 

print("Exercise 1: Load it") #!!!

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape())
print(df.columns.tolist())
print(df.dtypes)

print("Exercise 2: Filter by Region")

south = df[df["region"] == "South"]

print(len(south))
print(south.head())