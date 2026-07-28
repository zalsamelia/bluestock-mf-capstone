# bluestock-mf-capstone
Mutual Fund Analytics Platform - Bluestock Fintech Capstone Project
# Bluestock Mutual Fund Capstone

## Project Overview

This project was completed as part of the Bluestock Fintech Data Analyst Internship Capstone.

The objective of this project is to build a complete data analytics workflow, starting from raw data preparation, data cleaning, database creation, SQL analysis, exploratory data analysis (EDA), and business reporting. The project uses mutual fund datasets to analyze fund performance, investor behavior, and industry trends.

---

# Project Objectives

- Clean and prepare raw datasets for analysis.
- Build a structured SQLite database.
- Perform SQL-based business analysis.
- Conduct Exploratory Data Analysis (EDA).
- Generate business insights.
- Prepare data for dashboard development in Power BI.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Jupyter Notebook
- Git & GitHub

---

# Project Structure

```text
bluestock-mf-capstone/
│
├── analysis/
│   ├── eda.ipynb
│   └── figures/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── data_cleaning_plan.md
│   ├── data_cleaning_report.md
│   ├── data_dictionary.md
│   ├── data_quality_summary.md
│   ├── eda_report.md
│   └── business_insights.md
│
├── scripts/
│   ├── cleaning/
│   ├── load_to_db.py
│   └── run_query.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Datasets

The project uses ten datasets related to the Indian mutual fund industry.

| Dataset | Description |
|----------|-------------|
| Fund Master | Mutual fund master information |
| NAV History | Historical Net Asset Value (NAV) |
| Scheme Performance | Performance indicators |
| Investor Transactions | Investor transaction records |
| AUM | Assets Under Management |
| SIP | Monthly SIP inflows |
| Category Inflows | Net inflows by category |
| Industry Folios | Industry folio statistics |
| Portfolio Holdings | Mutual fund holdings |
| Benchmark Indices | Market benchmark data |

---

# Project Progress

## Day 1 – Data Cleaning

Completed:

- Data inspection
- Missing value checking
- Duplicate checking
- Data type validation
- Data standardization
- Clean dataset generation

Output:

- 10 cleaned CSV files
- Data Cleaning Report
- Data Quality Summary
- Data Cleaning Plan

---

## Day 2 – Database & SQL

Completed:

- SQLite database creation
- Star schema implementation
- SQL table creation
- Data loading
- SQL analytical queries
- Interactive SQL Query Runner
- Data Dictionary documentation

Output:

- SQLite database
- SQL schema
- SQL queries
- Interactive query runner
- Data Dictionary

---

## Day 3 – Exploratory Data Analysis

Completed:

- Dataset inspection
- Descriptive statistics
- Data quality assessment
- Exploratory Data Analysis
- Business visualizations
- EDA Report
- Business Insights

Visualizations include:

- Fund category distribution
- Top fund houses
- Risk category distribution
- Launch year trend
- Expense ratio distribution
- NAV distribution
- Average NAV analysis
- Fund performance analysis
- Investor transaction analysis
- Industry trend analysis

Output:

- EDA Notebook
- Visualization figures
- EDA Report
- Business Insights

---

# How to Run

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Data Cleaning

```bash
python scripts/cleaning/clean_01_fund_master.py
```

Repeat for the remaining cleaning scripts.

---

## 4. Create Database

```bash
python scripts/load_to_db.py
```

---

## 5. Run SQL Queries

```bash
python scripts/run_query.py
```

---

## 6. Open EDA Notebook

```text
analysis/eda.ipynb
```

Run all notebook cells to reproduce the exploratory analysis and generate visualization figures.

---

# Project Outputs

- Clean datasets
- SQLite database
- SQL analytical queries
- Interactive SQL query runner
- EDA notebook
- Visualization figures
- Data Dictionary
- EDA Report
- Business Insights

---

# Future Work

The next stage of this project is to build an interactive Power BI dashboard using the cleaned datasets and analytical outputs generated during this capstone.

---

# Author

**Zalsabilah Rezky Amelia Arep**

Data Analyst Intern – Bluestock Fintech Capstone