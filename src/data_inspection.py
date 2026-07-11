import pandas as pd

file_path = "data/raw/India_Tourism_2025.xlsx"

df = pd.read_excel(file_path)

print("Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nUnique States:")
print(df["State"].unique())

print("\nPurpose of Visit:")
print(df["Purpose of Visit"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())