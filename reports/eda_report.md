# Exploratory Data Analysis Report

## Project Overview

This report summarizes the results of the exploratory data analysis (EDA) conducted on the Bluestock Mutual Fund Capstone dataset. The purpose of this analysis is to understand the overall characteristics of the data, identify potential data quality issues, explore important business patterns, and prepare the dataset for dashboard development and further analysis.

The analysis was performed using Python with the Pandas and Matplotlib libraries.

---

# Dataset Summary

The project consists of multiple datasets representing different aspects of the mutual fund industry.

| Dataset | Description |
|----------|-------------|
| Fund Master | General information for each mutual fund scheme |
| NAV History | Historical Net Asset Value (NAV) records |
| Scheme Performance | Mutual fund performance indicators |
| Investor Transactions | Investor transaction history |
| AUM | Assets Under Management data |
| SIP | Monthly SIP inflow statistics |
| Category Inflow | Net inflow by mutual fund category |
| Industry Folio | Total investor folios |
| Portfolio Holdings | Fund portfolio composition |
| Benchmark Indices | Market benchmark index history |

---

# Data Quality Assessment

A data quality assessment was conducted before performing the exploratory analysis.

The following checks were completed:

- Missing value inspection
- Duplicate record inspection
- Data type validation
- Dataset dimension verification
- Statistical summary review

After the cleaning process completed during Day 2, all datasets were successfully standardized and prepared for analysis.

---

# Exploratory Data Analysis

## 1. Fund Master Analysis

The Fund Master dataset was analyzed to understand the characteristics of available mutual fund products.

The analysis included:

- Distribution of mutual fund categories
- Top 5 fund houses
- Risk category distribution
- Fund launch trend
- Expense ratio distribution

The visualizations provide an overview of product diversity, market participants, and investment characteristics.

---

## 2. NAV and Performance Analysis

The NAV and Performance datasets were analyzed to evaluate fund performance.

The analysis included:

- NAV distribution
- Top 5 average NAV
- Top 5 three-year return
- Top 5 Sharpe ratio
- Top 5 Assets Under Management (AUM)

These analyses highlight the variation in fund performance and identify high-performing investment products.

---

## 3. Investor Transaction Analysis

Investor transaction data was explored to understand investor behavior.

The analysis included:

- Transaction type distribution
- Top 5 states by transaction volume
- Investor age group distribution
- Payment mode distribution
- Average investment by age group

The results provide insights into investor demographics and transaction patterns.

---

## 4. Industry and Market Analysis

Industry-level datasets were analyzed to understand the overall mutual fund market.

The analysis included:

- Industry AUM trend
- Monthly SIP inflow trend
- Top 5 categories by net inflow
- Total folio trend
- Benchmark index trend

These analyses illustrate market growth, investor participation, and overall industry performance.

---

# Key Findings

Several important observations were identified during the analysis.

- Equity-based mutual funds represent a significant portion of the available investment products.
- A small number of fund houses manage a large number of mutual fund schemes.
- Mutual fund products cover various risk categories, allowing investors to select products based on their risk tolerance.
- Industry Assets Under Management (AUM) show continued growth throughout the observation period.
- Monthly SIP inflows indicate consistent investor participation in mutual fund investments.
- Investor transactions are distributed across multiple states and age groups, demonstrating broad market participation.
- Performance indicators such as NAV, three-year return, and Sharpe Ratio vary considerably across different schemes.

---

# Output

The exploratory data analysis produced multiple visualizations that were automatically saved in the following directory:

```text
analysis/
└── figures/
```

These visualizations will be used as supporting materials for dashboard development and business reporting.

---

# Conclusion

The exploratory data analysis successfully provided a comprehensive understanding of the Bluestock Mutual Fund datasets.

The datasets were confirmed to be suitable for further business analysis after the cleaning process. The visualizations generated during this stage reveal important trends related to mutual fund performance, investor behavior, and industry growth.

The cleaned datasets and EDA results will serve as the primary data source for the Power BI dashboard developed in the next stage of the project.