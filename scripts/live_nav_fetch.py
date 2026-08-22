"""
live_nav_fetch.py

This script retrieves live NAV (Net Asset Value)
history data from the public MFAPI service.

For each selected mutual fund scheme:

1. Fetch NAV history through API.
2. Convert JSON response into a DataFrame.
3. Clean and sort records by date.
4. Save results as CSV files inside data/raw.

The generated files can later be used for
ETL processing, database loading, and dashboard
development.

Project: Bluestock Mutual Fund Analytics
Module: External API Integration
"""

import requests
import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw")

# List of schemes to fetch
SCHEMES_TO_FETCH = {
    125497: "HDFC_Top_100_Direct",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

print("=" * 30)
print("LIVE NAV FETCH FROM mfapi.in")
print("=" * 30)

for code, name in SCHEMES_TO_FETCH.items():

    print(f"\nFetching: {name.replace('_', ' ')} (Code: {code})")

    try:

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        nav_data = data.get("data", [])

        if nav_data:

            df = pd.DataFrame(nav_data)

            df["date"] = pd.to_datetime(df["date"])

            df = (
                df.sort_values(
                    "date",
                    ascending=False
                )
                .reset_index(drop=True)
            )

            filename = (
                f"live_nav_{code}_{name}.csv"
            )

            filepath = (
                RAW_DATA_PATH / filename
            )

            df.to_csv(
                filepath,
                index=False
            )

            print(
                f"SUCCESS! {len(df)} records saved."
            )

            print(
                f"   ↳ Latest NAV: ₹{df.iloc[0]['nav']} "
                f"(Date: {df.iloc[0]['date'].strftime('%Y-%m-%d')})"
            )

        else:
            print(
                f"No NAV data found for code {code}."
            )

    except requests.exceptions.RequestException as e:

        print(
            f"FAILED to fetch data for {name}. "
            f"Error: {e}"
        )

print("\n" + "=" * 30)
print("LIVE NAV FETCH COMPLETED!")
print("=" * 30)