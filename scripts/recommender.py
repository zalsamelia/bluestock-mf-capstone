from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "clean_scheme_performance.csv"


def load_fund_data():
    """Load fund performance data from the processed CSV file."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    required_columns = [
        "amfi_code",
        "scheme_name",
        "sharpe_ratio",
        "risk_grade"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    return df


def recommend_funds(risk_appetite, top_n=3):
    """
    Recommend funds based on investor risk appetite.

    Risk appetite mapping:
    Low -> Low
    Moderate -> Moderate
    High -> High
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
        print(f"No funds found for risk appetite: {risk_appetite}")
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


def main():
    print("Bluestock Mutual Fund Recommender")
    print("---------------------------------")

    risk_input = input(
        "Enter risk appetite (Low / Moderate / High): "
    )

    try:
        recommendations = recommend_funds(risk_input)

        if recommendations is not None:
            print("\nTop 3 Fund Recommendations:")
            print(
                recommendations.to_string(index=False)
            )

    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()