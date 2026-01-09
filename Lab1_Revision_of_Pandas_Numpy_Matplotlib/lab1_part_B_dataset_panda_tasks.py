import kagglehub
import pandas as pd
import numpy as np
import os
import glob

# Download dataset using kagglehub
path = kagglehub.dataset_download("ealaxi/paysim1")
print("Path to dataset files:", path)

# 1. Select CSV dataset 
csv_files = glob.glob(os.path.join(path, "*.csv"))

df = pd.read_csv(csv_files[0])

print("\nDataset loaded successfully.")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# 2. Explore size, shape, and data types
print("\nDataset Shape (rows, columns):")
print(df.shape)

print("\nDataset Size (total elements):")
print(df.size)

print("\nData Types of Each Column:")
print(df.dtypes)

# 3. Identify null / missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Replace missing values by appropriate values
for column in df.columns:
    if df[column].dtype == "object":
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df[column].fillna(df[column].mean(), inplace=True)

print("\nMissing values replaced.")

# 5. Remove null values 
df_cleaned = df.dropna()

print("\nRemaining missing values after cleaning:")
print(df_cleaned.isnull().sum())

# 6. Display first 10 rows
print("\nFirst 10 rows of the dataset:")
print(df_cleaned.head(10))

# 7. Display last 5 rows
print("\nLast 5 rows of the dataset:")
print(df_cleaned.tail(5))
