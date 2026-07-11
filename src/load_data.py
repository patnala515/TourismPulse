import pandas as pd

file_path = "data/raw/India_Tourism_2025.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)