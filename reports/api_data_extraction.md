# REST API & JSON Data Extraction

## 1. Objective

This task demonstrates how a public REST API can be accessed, how its JSON response can be inspected, and how the extracted data can be transformed into a structured CSV file for analysis.

## 2. API Used

A public cryptocurrency price API was used to retrieve the current prices of Bitcoin and Ethereum in USD and INR.

## 3. HTTP Method

The API was accessed using the GET method because the task only required retrieving data from the public API.

## 4. JSON Response

The API returned a nested JSON object containing two assets:

- Bitcoin
  - USD price
  - INR price
- Ethereum
  - USD price
  - INR price

The response was saved in its original form as:

`api/raw/api_response.json`

## 5. JSON to CSV Transformation

The nested JSON response was transformed into a tabular structure containing three columns:

- `asset`
- `price_usd`
- `price_inr`

The resulting dataset contains:

| Asset | Price USD | Price INR |
|---|---:|---:|
| Bitcoin | 69,588.00 | 6,648,854 |
| Ethereum | 2,269.12 | 216,804 |

The processed dataset was saved as:

`api/processed/api_data.csv`

## 6. Result

The API request was successfully executed, the JSON response was inspected, and the extracted data was converted into a structured CSV dataset suitable for further analysis.

## 7. Output Files

- `api/raw/api_response.json` — original API response
- `api/processed/api_data.csv` — processed CSV dataset
- `scripts/api_extraction.py` — Python script used for API extraction and transformation