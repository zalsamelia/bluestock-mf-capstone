"""
==========================================================
Bluestock Mutual Fund Capstone
Day 2 - Data Cleaning

Dataset:
06_industry_folio_count.csv

Purpose:
This script performs data profiling, quality assessment,
cleaning, validation, and export processes for the
Industry Folio Count dataset.

Main Tasks:
1. Load raw dataset
2. Inspect dataset structure
3. Perform data quality assessment
4. Convert date column to datetime
5. Validate numeric columns
6. Export cleaned dataset

Output:
clean_industry_folio_count.csv

==========================================================
"""

import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

FOLIO_FILE = RAW_DATA_PATH / "06_industry_folio_count.csv"


def load_dataset():
    """
    Load the Industry Folio Count dataset.

    Returns
    -------
    pandas.DataFrame
        Raw dataset loaded from CSV file.
    """
    return pd.read_csv(FOLIO_FILE)


def inspect_dataset(df):
    """
    Display dataset structure and summary statistics.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to inspect.
    """

    print("\n" + "=" * 60)
    print("Industry Folio Count Dataset")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    for column in df.columns:
        print(f"- {column}")

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nDataset Information")
    df.info()

    print("\nStatistical Summary")
    print(df.describe(include="all"))


def assess_data_quality(df):
    """
    Perform data quality assessment.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to evaluate.
    """

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)
    print(df.isnull().sum())

    print("\n" + "=" * 60)
    print("Duplicate Records")
    print("=" * 60)
    print(f"Duplicate Rows : {df.duplicated().sum()}")

    print("\n" + "=" * 60)
    print("Month Range")
    print("=" * 60)

    print(f"Earliest Month : {df['month'].min()}")
    print(f"Latest Month   : {df['month'].max()}")

    print("\n" + "=" * 60)
    print("Total Folios Validation")
    print("=" * 60)

    print(f"Minimum Total Folios : {df['total_folios_crore'].min()}")
    print(f"Maximum Total Folios : {df['total_folios_crore'].max()}")


def clean_dataset(df):
    """
    Clean and standardize dataset.

    Cleaning Steps
    --------------
    1. Convert month column to datetime
    2. Validate numeric columns
    3. Handle invalid values using coercion

    Parameters
    ----------
    df : pandas.DataFrame
        Raw dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    df["month"] = pd.to_datetime(df["month"])

    numeric_columns = [
        "total_folios_crore",
        "equity_folios_crore",
        "debt_folios_crore",
        "hybrid_folios_crore",
        "others_folios_crore"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    print("\n" + "=" * 60)
    print("Data Cleaning Summary")
    print("=" * 60)

    print("✓ Month converted to datetime.")
    print("✓ Numeric columns validated.")
    print("✓ Dataset cleaned successfully.")

    return df


def save_dataset(df):
    """
    Save cleaned dataset into processed folder.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned dataset.
    """

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_industry_folio_count.csv"
    )

    df.to_csv(output_file, index=False)

    print(f"\nDataset saved to:\n{output_file}")


def main():
    """
    Execute complete ETL cleaning workflow.
    """

    folio_df = load_dataset()

    inspect_dataset(folio_df)

    assess_data_quality(folio_df)

    folio_df = clean_dataset(folio_df)

    save_dataset(folio_df)


if __name__ == "__main__":
    main()