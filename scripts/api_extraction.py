"""
API Extraction Script

This script fetches cryptocurrency price data from the CoinGecko API,
stores the raw JSON response, and converts the data into CSV format
for further analysis.

Project:
    Bluestock Mutual Fund Analytics Dashboard

Author:
    Zalsabilah

Output:
    - api/raw/api_response.json
    - api/processed/api_data.csv
"""

import json
from pathlib import Path

import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "api" / "raw"
PROCESSED_DIR = BASE_DIR / "api" / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd,inr"
}


def fetch_api_data():
    """
    Fetch cryptocurrency price data from the CoinGecko API.

    Sends a GET request to the CoinGecko public API and retrieves
    the latest price information for Bitcoin and Ethereum in USD and INR.

    Returns:
        dict:
            JSON response containing cryptocurrency prices.

    Raises:
        requests.exceptions.HTTPError:
            If the API request fails.
    """

    response = requests.get(API_URL, params=PARAMS, timeout=30)

    response.raise_for_status()

    return response.json()


def save_raw_json(data):
    """
    Save raw API response as a JSON file.

    Parameters:
        data (dict):
            JSON response returned from the API.

    Returns:
        Path:
            Path to the saved JSON file.
    """

    output_file = RAW_DIR / "api_response.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return output_file


def convert_json_to_csv(data):
    """
    Convert API JSON response into CSV format.

    Extracts cryptocurrency names and their corresponding
    USD and INR prices, then stores them in a CSV file.

    Parameters:
        data (dict):
            JSON response returned from the API.

    Returns:
        Path:
            Path to the generated CSV file.
    """

    rows = []

    for asset, values in data.items():
        row = {
            "asset": asset,
            "price_usd": values.get("usd"),
            "price_inr": values.get("inr")
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    output_file = PROCESSED_DIR / "api_data.csv"

    df.to_csv(output_file, index=False)

    return output_file


def main():
    """
    Execute the complete API extraction workflow.

    Workflow:
        1. Fetch cryptocurrency data from API.
        2. Save raw JSON response.
        3. Convert JSON data into CSV format.
        4. Save processed output files.
        5. Display status messages.
    """

    print("Fetching data from public API...")

    data = fetch_api_data()

    print("API request successful.")
    print("JSON response:")
    print(json.dumps(data, indent=4))

    raw_file = save_raw_json(data)
    csv_file = convert_json_to_csv(data)

    print(f"\nRaw JSON saved to: {raw_file}")
    print(f"Processed CSV saved to: {csv_file}")


if __name__ == "__main__":
    main()