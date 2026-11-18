# Self Assessment Questions:
# 1. A Boolean filter picks rows of data based on conditionals.

# It then checks for True and False based on conditions.

# 2. df[“revenue”] returns a Series, which is 1D.
# df[[“revenue”]] returns a DataFrame, which is 2D.
# It matters because when you are performing operations, it requires a DataFrame instead of a Series.

# 3. My one reason would be that repetitive tasks would become so much faster and more efficent.
# Using pandas enables sorting of different categories to be easier. 

print("Exercise 1: Load it") #!!!

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("Exercise 2: Filter by Region") #!!!

south = df[df["region"] == "South"]

print(len(south))
print(south.head())

print("Exercise 3: Top 5 by Revenue") #!!!

top_5 = df.sort_values("revenue", ascending = False).head(5)

print(top_5)

print("Exercise 4: Two-Condition Filter") #!!!

big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print(len(big_south))

print("Exercise 5: A New Column") #!!!

df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())

print("Exercise 6: Unique values") #!!!

print(df["region"].unique())
print(df["region"].value_counts().plot)

print("Exercise 7: Select Columns") #!!!

df_subset = df[["region", "product", "revenue"]]
print(df_subset.shape)

print("Exercise 8: Save") #!!!

df.to_csv("data/explored.csv", index = False)