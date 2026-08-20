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
    response = requests.get(API_URL, params=PARAMS, timeout=30)

    response.raise_for_status()

    return response.json()


def save_raw_json(data):
    output_file = RAW_DIR / "api_response.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return output_file


def convert_json_to_csv(data):
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