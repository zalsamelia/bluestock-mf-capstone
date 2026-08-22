"""
recommender.py

Bluestock Mutual Fund Recommendation Engine.

This module provides a simple rule-based recommendation system
that suggests mutual funds based on an investor's risk appetite.

The recommendation process uses:
- Risk category filtering
- Sharpe Ratio ranking
- Top-N selection

Risk Appetite Mapping:
- Low      -> Low Risk Funds
- Moderate -> Moderate Risk Funds
- High     -> High Risk Funds

Data Source:
data/processed/clean_scheme_performance.csv

Project:
Bluestock Mutual Fund Analytics Platform

"""

from pathlib import Path
import pandas as pd


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "clean_scheme_performance.csv"
)


# ==========================================================
# Data Loading
# ==========================================================

def load_fund_data():
    """
    Load and validate mutual fund performance data.

    The function reads the cleaned scheme performance dataset
    and verifies whether all required columns are available.

    Returns
    -------
    pandas.DataFrame
        Cleaned mutual fund performance dataset.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.

    ValueError
        If required columns are missing.
    """

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Data file not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    required_columns = [
        "amfi_code",
        "scheme_name",
        "sharpe_ratio",
        "risk_grade"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: "
            f"{', '.join(missing_columns)}"
        )

    return df


# ==========================================================
# Recommendation Engine
# ==========================================================

def recommend_funds(risk_appetite, top_n=3):
    """
    Recommend mutual funds based on investor risk appetite.

    Funds are filtered according to risk category and then
    ranked by Sharpe Ratio in descending order.

    Parameters
    ----------
    risk_appetite : str
        Investor risk preference.
        Accepted values:
        - Low
        - Moderate
        - High

    top_n : int, default=3
        Number of recommendations to return.

    Returns
    -------
    pandas.DataFrame or None
        Top recommended funds sorted by Sharpe Ratio.

    Examples
    --------
    >>> recommend_funds("Moderate")
    """

    df = load_fund_data()

    risk_appetite = risk_appetite.strip().title()

    valid_risk_levels = {
        "Low": ["Low"],
        "Moderate": ["Moderate"],
        "High": ["High"]
    }

    if risk_appetite not in valid_risk_levels:
        print(
            "Invalid risk appetite. "
            "Please choose Low, Moderate, or High."
        )
        return None

    selected_risk = valid_risk_levels[risk_appetite]

    recommendations = df[
        df["risk_grade"].isin(selected_risk)
    ].copy()

    if recommendations.empty:
        print(
            f"No funds found for risk appetite: "
            f"{risk_appetite}"
        )
        return None

    recommendations["sharpe_ratio"] = pd.to_numeric(
        recommendations["sharpe_ratio"],
        errors="coerce"
    )

    recommendations = recommendations.dropna(
        subset=["sharpe_ratio"]
    )

    recommendations = recommendations.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(top_n)

    return recommendations[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]


# ==========================================================
# Main Program
# ==========================================================

def main():
    """
    Execute the recommendation workflow.

    Prompts the user for risk appetite and displays
    the top recommended mutual funds.
    """

    print("Bluestock Mutual Fund Recommender")
    print("---------------------------------")

    risk_input = input(
        "Enter risk appetite (Low / Moderate / High): "
    )

    try:

        recommendations = recommend_funds(
            risk_input
        )

        if recommendations is not None:

            print("\nTop Fund Recommendations:")

            print(
                recommendations.to_string(
                    index=False
                )
            )

    except (
        FileNotFoundError,
        ValueError
    ) as error:

        print(
            f"\nError: {error}"
        )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()