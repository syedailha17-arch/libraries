import pandas as pd

# Create
df = pd.DataFrame(data)

# Read
pd.read_csv("file.csv")

# View
df.head()
df.tail()

# Info
df.shape
df.columns
df.info()
df.describe()

# Select
df["col"]
df[["c1", "c2"]]

# Rows
df.loc[0]
df.iloc[0]

# Specific value
df.loc[0, "col"]
df.iloc[0, 1]

# Filter
df[df["Age"] > 20]
df[(cond1) & (cond2)]
df[(cond1) | (cond2)]

# Add column
df["new"] = values

# Modify
df.loc[0, "Age"] = 25

# Delete
df.drop("col", axis=1)
df.drop(0)

# Sort
df.sort_values("Age")
df.sort_values("Age", ascending=False)

# Missing values
df.isnull()
df.dropna()
df.fillna(0)

# Statistics
df["Age"].mean()
df["Age"].sum()
df["Age"].max()
df["Age"].min()

# Grouping
df.groupby("City").mean()

# Strings
df["Name"].str.upper()
df["Name"].str.contains("A")

# Rename
df.rename(columns={"old":"new"})

# Unique
df["City"].unique()
df["City"].value_counts()

# Merge
pd.merge(df1, df2, on="ID")

# Concatenate
pd.concat([df1, df2])

# Index
df.set_index("Name")
df.reset_index()

# Save
df.to_csv("out.csv", index=False)