"""
Fund Master Exploration Script

This script explores the fund master dataset and displays
basic information including:

- Total number of schemes
- Fund houses
- Categories
- Sub-categories
- Risk categories
"""

from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw")


def load_fund_master():
    """
    Load the fund master dataset.

    Returns:
        pandas.DataFrame:
            Fund master data.
    """
    return pd.read_csv(RAW_DATA_PATH / "01_fund_master.csv")


def display_unique_values(df, column_name, title):
    """
    Display unique values from a selected column.

    Parameters:
        df (DataFrame):
            Source dataframe.

        column_name (str):
            Column to analyze.

        title (str):
            Section title.
    """

    print(f"\n{title}")

    for value in df[column_name].dropna().unique():
        print(f"  - {value}")


def main():
    """
    Execute fund master exploration workflow.
    """

    df = load_fund_master()

    print("=" * 70)
    print("FUND MASTER EXPLORATION")
    print("=" * 70)

    print(f"\nTotal Schemes: {len(df)}")

    display_unique_values(
        df,
        "fund_house",
        "Unique Fund Houses:"
    )

    display_unique_values(
        df,
        "category",
        "Unique Categories:"
    )

    display_unique_values(
        df,
        "sub_category",
        "Unique Sub-Categories:"
    )

    display_unique_values(
        df,
        "risk_category",
        "Unique Risk Categories:"
    )

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()