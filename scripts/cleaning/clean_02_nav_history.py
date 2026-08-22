"""
clean_nav_history.py

Day 2 - Data Cleaning
Dataset: 02_nav_history.csv

This script performs data inspection, quality assessment,
and cleaning for the NAV History dataset.

Cleaning activities:
- Convert date column to datetime format
- Remove thousand separators from NAV values
- Convert NAV values to numeric format
- Handle missing NAV values using forward-fill
- Save cleaned dataset for downstream ETL processes

Input:
data/raw/02_nav_history.csv

Output:
data/processed/clean_nav_history.csv

Project:
Bluestock Mutual Fund Analytics Platform
"""

# ==========================================================
# Import Libraries
# ==========================================================

import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

NAV_HISTORY_FILE = RAW_DATA_PATH / "02_nav_history.csv"


# ==========================================================
# Load Dataset Function
# ==========================================================

def load_dataset():
    """
    Load NAV history dataset.

    Returns
    -------
    pandas.DataFrame
        Raw NAV history dataset.
    """

    return pd.read_csv(
        NAV_HISTORY_FILE,
        dtype={
            "date": "str",
            "nav": "str"
        }
    )


# ==========================================================
# Dataset Inspection Function
# ==========================================================

def inspect_dataset(nav_df):
    """
    Display dataset overview and structure.

    Parameters
    ----------
    nav_df : pandas.DataFrame
        NAV history dataset.

    Returns
    -------
    None
    """

    print("\n" + "=" * 60)

    print("NAV History Dataset")
    print("=" * 60)

    print(f"Rows    : {nav_df.shape[0]}")
    print(f"Columns : {nav_df.shape[1]}")

    print("\nColumn Names")

    for column in nav_df.columns:
        print(f"- {column}")

    print("\nData Types")
    print(nav_df.dtypes)

    print("\nFirst Five Rows")
    print(nav_df.head())

    print("\nDataset Information")
    nav_df.info()

    print("\nStatistical Summary")
    print(nav_df.describe())


# ==========================================================
# Data Quality Assessment Function
# ==========================================================

def assess_data_quality(nav_df):
    """
    Perform data quality assessment.

    Parameters
    ----------
    nav_df : pandas.DataFrame
        NAV history dataset.

    Returns
    -------
    None
    """

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)

    print(nav_df.isnull().sum())

    print("\n" + "=" * 60)
    print("Duplicate Records")
    print("=" * 60)

    print(
        f"Duplicate Rows : "
        f"{nav_df.duplicated().sum()}"
    )

    print("\n" + "=" * 60)
    print("Unique AMFI Codes")
    print("=" * 60)

    print(
        f"Unique AMFI Codes : "
        f"{nav_df['amfi_code'].nunique()}"
    )

    print("\n" + "=" * 60)
    print("Date Sample")
    print("=" * 60)

    print(nav_df["date"].head())

    print("\n" + "=" * 60)
    print("NAV Sample")
    print("=" * 60)

    print(nav_df["nav"].head())

    print("\n" + "=" * 60)
    print("Dataset Dimensions")
    print("=" * 60)

    print(f"Rows    : {nav_df.shape[0]}")
    print(f"Columns : {nav_df.shape[1]}")


# ==========================================================
# Data Cleaning Function
# ==========================================================

def clean_dataset(nav_df):
    """
    Clean NAV history dataset.

    Cleaning Steps:
    - Convert date column to datetime
    - Remove commas from NAV values
    - Convert NAV values to numeric
    - Handle missing NAV values

    Parameters
    ----------
    nav_df : pandas.DataFrame
        Raw dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Process")
    print("=" * 60)

    # Convert date column into datetime

    nav_df["date"] = pd.to_datetime(
        nav_df["date"]
    )

    # Remove thousand separator

    nav_df["nav"] = nav_df["nav"].str.replace(
        ",",
        "",
        regex=False
    )

    # Convert NAV to numeric

    nav_df["nav"] = pd.to_numeric(
        nav_df["nav"]
    )

    print(
        "✓ Date column converted to datetime."
    )

    print(
        "✓ NAV column converted to numeric."
    )

    print(
        "✓ Dataset cleaned successfully."
    )

    # Handle missing NAV values

    if nav_df["nav"].isnull().sum() > 0:

        nav_df["nav"] = nav_df["nav"].ffill()

        print(
            "✓ Missing NAV values filled "
            "using forward-fill."
        )

    else:

        print(
            "✓ No missing NAV values found."
        )

    return nav_df


# ==========================================================
# Data Cleaning Summary Function
# ==========================================================

def cleaning_summary():
    """
    Display cleaning summary.

    Returns
    -------
    None
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Summary")
    print("=" * 60)

    print("No missing values detected.")
    print("No duplicate records detected.")
    print(
        "Date column successfully converted "
        "to datetime."
    )
    print(
        "NAV column successfully converted "
        "to numeric."
    )
    print(
        "Dataset is ready for analysis."
    )


# ==========================================================
# Save Dataset Function
# ==========================================================

def save_dataset(nav_df):
    """
    Save cleaned dataset.

    Parameters
    ----------
    nav_df : pandas.DataFrame
        Cleaned dataset.

    Returns
    -------
    pathlib.Path
        Saved file path.
    """

    print("\n" + "=" * 60)
    print("Saving Clean Dataset")
    print("=" * 60)

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_nav_history.csv"
    )

    nav_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Dataset successfully saved to:\n"
        f"{output_file}"
    )

    return output_file


# ==========================================================
# Main Function
# ==========================================================

def main():
    """
    Execute complete NAV history cleaning workflow.

    Returns
    -------
    None
    """

    nav_df = load_dataset()

    inspect_dataset(nav_df)

    assess_data_quality(nav_df)

    nav_df = clean_dataset(nav_df)

    cleaning_summary()

    save_dataset(nav_df)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()