"""
Data Ingestion Script

This script scans all CSV files located in the data/raw directory
and generates a basic ingestion report.

The report includes:
    - Dataset name
    - Dataset shape (rows and columns)
    - Data types
    - First five records

Project:
    Bluestock Mutual Fund Analytics Dashboard

"""

from pathlib import Path

import pandas as pd


# Path to raw datasets
RAW_DATA_PATH = Path("data/raw")


def get_csv_files():
    """
    Retrieve all CSV files from the raw data directory.

    Returns:
        list:
            List of CSV file paths.
    """
    return sorted(RAW_DATA_PATH.glob("*.csv"))


def generate_ingestion_report(file_path):
    """
    Generate a basic data ingestion report for a CSV file.

    Parameters:
        file_path (Path):
            Path to the CSV file.
    """

    df = pd.read_csv(file_path)

    print(f"\nDataset: {file_path.name}")
    print(f"Shape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst Five Rows:")
    print(df.head())

    print("-" * 70)


def main():
    """
    Execute the data ingestion workflow.

    Steps:
        1. Locate all CSV files in data/raw.
        2. Generate a report for each dataset.
        3. Display dataset structure and sample records.
    """

    csv_files = get_csv_files()

    if not csv_files:
        print("No CSV files found in data/raw folder")
        return

    print("=" * 70)
    print("DATA INGESTION REPORT")
    print("=" * 70)

    for file in csv_files:
        generate_ingestion_report(file)


if __name__ == "__main__":
    main()