import pandas as pd

# ==========================
# PANDAS SERIES NOTES
# ==========================

# A Series is a 1-dimensional labeled array

# Creating a Series
s = pd.Series([10, 20, 30, 40])
print(s)

# Creating a Series with custom indexes
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# Creating a Series from a dictionary
grades = {
    "Math": 95,
    "Physics": 90,
    "Chemistry": 88
}

s = pd.Series(grades)
print(s)

# --------------------------
# Accessing data
# --------------------------

print(s["Math"])      # Access by label
print(s.iloc[0])      # Access by position

# Multiple values
print(s[["Math", "Physics"]])

# --------------------------
# Attributes
# --------------------------

print(s.index)        # Labels
print(s.values)       # Data
print(s.dtype)        # Data type
print(s.shape)        # Dimensions
print(s.size)         # Number of elements

# --------------------------
# Updating values
# --------------------------

s["Math"] = 100
print(s)

# Add new value
s["Biology"] = 92
print(s)

# --------------------------
# Vectorized operations
# --------------------------

numbers = pd.Series([1, 2, 3, 4])

print(numbers + 10)
print(numbers * 2)
print(numbers ** 2)

# --------------------------
# Filtering
# --------------------------

print(numbers[numbers > 2])

# --------------------------
# Checking values
# --------------------------

print(numbers > 2)

# --------------------------
# Useful methods
# --------------------------

print(numbers.sum())
print(numbers.mean())
print(numbers.max())
print(numbers.min())
print(numbers.std())

# --------------------------
# Missing values
# --------------------------

s = pd.Series([1, None, 3, None])

print(s.isna())
print(s.notna())

print(s.fillna(0))
print(s.dropna())

# --------------------------
# Sorting
# --------------------------

s = pd.Series([50, 10, 40, 20])

print(s.sort_values())
print(s.sort_values(ascending=False))

# --------------------------
# Value counts
# --------------------------

letters = pd.Series(["A", "B", "A", "C", "A"])

print(letters.value_counts())

# --------------------------
# Apply function
# --------------------------

numbers = pd.Series([1, 2, 3, 4])

print(numbers.apply(lambda x: x * 10))

# --------------------------
# Convert Series
# --------------------------

print(numbers.tolist())
print(numbers.to_dict())