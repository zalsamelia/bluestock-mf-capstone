"""
load_query.py

Bluestock Mutual Fund Analytics
Interactive SQL Query Runner

This script provides an interactive command-line interface
for executing predefined SQL queries against the Bluestock
Mutual Fund SQLite database.

The objective of this tool is to allow users, analysts,
and project reviewers to explore key business insights
without manually writing SQL statements.

Available analyses include:
- Top funds by AUM
- Lowest expense ratio funds
- Highest Sharpe ratio funds
- Average returns by category
- Transaction analysis
- Investor segmentation
- NAV analysis
- Benchmark outperformance analysis

Database:
bluestock_mf.db

Project:
Bluestock Mutual Fund Analytics Platform

"""

# ==========================================================
# Import Libraries
# ==========================================================

import sqlite3
import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"


# ==========================================================
# Database Connection
# ==========================================================

connection = sqlite3.connect(DATABASE_PATH)


# ==========================================================
# Predefined SQL Queries
# ==========================================================

queries = {

    1: {
        "title": "Top 5 Funds by Assets Under Management (AUM)",
        "sql": """
            SELECT
                scheme_name,
                fund_house,
                aum_crore
            FROM fact_performance
            ORDER BY aum_crore DESC
            LIMIT 5;
        """
    },

    2: {
        "title": "Top 5 Funds with Lowest Expense Ratio",
        "sql": """
            SELECT
                scheme_name,
                fund_house,
                expense_ratio_pct
            FROM fact_performance
            ORDER BY expense_ratio_pct ASC
            LIMIT 5;
        """
    },

    3: {
        "title": "Top 5 Highest Sharpe Ratio",
        "sql": """
            SELECT
                scheme_name,
                sharpe_ratio,
                risk_grade
            FROM fact_performance
            ORDER BY sharpe_ratio DESC
            LIMIT 5;
        """
    },

    4: {
        "title": "Average 3-Year Return by Category",
        "sql": """
            SELECT
                category,
                ROUND(AVG(return_3yr_pct),2) AS average_return
            FROM fact_performance
            GROUP BY category
            ORDER BY average_return DESC;
        """
    },

    5: {
        "title": "Transactions by State",
        "sql": """
            SELECT
                state,
                COUNT(*) AS total_transactions
            FROM fact_transactions
            GROUP BY state
            ORDER BY total_transactions DESC;
        """
    },

    6: {
        "title": "Average Investment by Age Group",
        "sql": """
            SELECT
                age_group,
                ROUND(AVG(amount_inr),2) AS average_investment
            FROM fact_transactions
            GROUP BY age_group
            ORDER BY average_investment DESC;
        """
    },

    7: {
        "title": "Investor Distribution by City Tier",
        "sql": """
            SELECT
                city_tier,
                COUNT(*) AS total_transactions
            FROM fact_transactions
            GROUP BY city_tier;
        """
    },

    8: {
        "title": "Monthly Transaction Volume",
        "sql": """
            SELECT
                strftime('%Y-%m', transaction_date) AS month,
                COUNT(*) AS total_transactions
            FROM fact_transactions
            GROUP BY month
            ORDER BY month;
        """
    },

    9: {
        "title": "Average NAV by Fund",
        "sql": """
            SELECT
                d.scheme_name,
                ROUND(AVG(f.nav),2) AS average_nav
            FROM fact_nav f
            JOIN dim_fund d
            ON f.amfi_code = d.amfi_code
            GROUP BY d.scheme_name
            ORDER BY average_nav DESC;
        """
    },

    10: {
        "title": "Fund Outperformance Against Benchmark",
        "sql": """
            SELECT
                scheme_name,
                return_3yr_pct,
                benchmark_3yr_pct,
                ROUND(
                    return_3yr_pct - benchmark_3yr_pct,
                    2
                ) AS excess_return
            FROM fact_performance
            ORDER BY excess_return DESC;
        """
    }

}


# ==========================================================
# Helper Functions
# ==========================================================

def display_menu():
    """
    Display available SQL queries.

    Returns
    -------
    None
    """

    print("\n")
    print("=" * 45)
    print("Bluestock Mutual Fund Analytics")
    print("Interactive SQL Query Runner")
    print("=" * 45)

    for number, query in queries.items():
        print(f"{number}. {query['title']}")

    print("0. Exit")


def execute_query(choice):
    """
    Execute selected SQL query and display results.

    Parameters
    ----------
    choice : int
        Query number selected by the user.

    Returns
    -------
    None
    """

    print("\n")
    print("=" * 45)
    print(queries[choice]["title"])
    print("=" * 45)

    result = pd.read_sql_query(
        queries[choice]["sql"],
        connection
    )

    print(result)


# ==========================================================
# Main Program
# ==========================================================

def main():
    """
    Run the interactive query runner.

    Users can select predefined analytical
    queries and view results directly from
    the SQLite database.
    """

    while True:

        display_menu()

        try:
            choice = int(
                input("\nSelect a query (0-10): ")
            )

        except ValueError:
            print(
                "\nPlease enter a valid number."
            )
            continue

        if choice == 0:
            print(
                "\nProgram closed successfully."
            )
            break

        if choice not in queries:
            print(
                "\nInvalid selection."
            )
            continue

        execute_query(choice)

        input(
            "\nPress Enter to continue..."
        )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    try:
        main()

    finally:

        connection.close()

        print(
            "\nDatabase connection closed."
        )