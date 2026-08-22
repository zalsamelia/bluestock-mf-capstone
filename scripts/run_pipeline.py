"""
Bluestock Mutual Fund Capstone

Master Pipeline Runner

This script executes the complete ETL workflow:

1. Data Cleaning
2. Database Loading
3. Database Verification

Author: Zalsabilah Rezky
"""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent

PIPELINE_STEPS = [
    "cleaning/clean_01_fund_master.py",
    "cleaning/clean_02_nav_history.py",
    "cleaning/clean_03_aum.py",
    "cleaning/clean_04_sip.py",
    "cleaning/clean_05_category.py",
    "cleaning/clean_06_folio.py",
    "cleaning/clean_07_performance.py",
    "cleaning/clean_08_transactions.py",
    "cleaning/clean_09_portfolio.py",
    "cleaning/clean_10_benchmark.py",

    "load_to_db.py",
    "verify_database.py"
]


def run_script(script_name):
    """
    Execute a Python script and stop pipeline if it fails.
    """

    script_path = PROJECT_ROOT / script_name

    print("\n" + "=" * 60)
    print(f"Running: {script_name}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, str(script_path)]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script_name} failed.")
        sys.exit(1)

    print(f"\nSUCCESS: {script_name} completed.")


def main():
    """
    Execute complete Bluestock ETL pipeline.
    """

    print("\n" + "=" * 60)
    print("BLUESTOCK MUTUAL FUND PIPELINE")
    print("=" * 60)

    for step in PIPELINE_STEPS:
        run_script(step)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()