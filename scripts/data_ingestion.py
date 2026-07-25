import pandas as pd
from pathlib import Path

# Define path
RAW_DATA_PATH = Path("data/raw")

# Find all CSV files
csv_files = sorted(RAW_DATA_PATH.glob("*.csv"))

# Check if files exist
if not csv_files:
    print("No CSV files found in data/raw folder")
    exit()

print("=" * 70)
print("DATA INGESTION REPORT")
print("=" * 70)

# Loop through each CSV file
for file in csv_files:
    df = pd.read_csv(file)

    print(f"\nDataset: {file.name}")
    print(f"Shape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst Five Rows:")
    print(df.head())

    print("-" * 70)