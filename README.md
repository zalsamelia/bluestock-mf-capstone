# Mutual Fund Analytics Platform
### Bluestock Fintech Data Analyst Capstone Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

# Project Overview

This project was completed as part of the **Bluestock Fintech Data Analyst Internship Capstone Program**.

The objective of this project is to build a complete end-to-end data analytics workflow using mutual fund industry data. The workflow covers data cleaning, database creation, SQL analysis, exploratory data analysis (EDA), business insight generation, and interactive dashboard development using Power BI.

The final outcome is an interactive dashboard that provides insights into mutual fund performance, investor behavior, fund allocation, Assets Under Management (AUM), SIP trends, and investment distribution across India.

---

# Project Objectives

- Clean and prepare raw mutual fund datasets
- Perform data quality assessment
- Build a structured SQLite database
- Execute SQL-based business analysis
- Conduct Exploratory Data Analysis (EDA)
- Generate business insights
- Develop an interactive Power BI dashboard
- Present data-driven recommendations

---

# Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Git
- GitHub

---

# Project Structure

```text
bluestock-mf-capstone/
│
├── analysis/
│   ├── EDA.ipynb
│   └── figures/
│
├── dashboard/
│   ├── Mutual_Fund_Dashboard.pbix
│   └── dashboard_preview.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── dashboard.pdf
│
├── reports/
│   ├── business_insights.md
│   ├── data_cleaning_plan.md
│   ├── data_cleaning_report.md
│   ├── data_dictionary.md
│   ├── data_quality_summary.md
│   └── eda_report.md
│
├── scripts/
│
├── sql/
│
├── .gitignore
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

---

# Datasets

The project uses ten datasets representing different aspects of the Indian Mutual Fund industry.

| Dataset | Description |
|----------|-------------|
| Fund Master | Mutual fund master information |
| NAV History | Historical NAV prices |
| Scheme Performance | Fund performance metrics |
| Investor Transactions | Investor transaction records |
| Assets Under Management | AUM statistics |
| Monthly SIP Inflows | SIP investment trends |
| Category Inflows | Net inflow by category |
| Industry Folios | Investor folio statistics |
| Portfolio Holdings | Mutual fund holdings |
| Benchmark Indices | Benchmark performance |

---

# Database Design

The project uses SQLite as the analytical database.

The database follows a simplified star schema consisting of:

- Dimension Tables
  - Fund
  - Date

- Fact Tables
  - Performance
  - Transactions
  - NAV

A separate AUM fact table was not created because each performance record already contains the corresponding AUM value, reducing redundancy while maintaining a clean analytical structure.

---

# Exploratory Data Analysis

EDA was conducted to understand the characteristics of the mutual fund market and identify investment trends.

The analysis includes:

- Data quality assessment
- Missing value analysis
- Distribution analysis
- Fund category analysis
- Performance analysis
- Risk analysis
- Expense ratio analysis
- NAV analysis
- Investor transaction analysis
- Industry trend analysis

---

# Dashboard Features

The interactive Power BI dashboard contains:

- KPI Cards
  - Total Assets Under Management
  - Total Mutual Fund Schemes
  - Registered Investors
  - Average 3-Year Return

- Top Fund Houses by AUM

- Average 3-Year Return by Category

- Monthly SIP Trend

- Fund Allocation

- Top States by Investment

- Investor Demographics

---

# Dashboard Preview

> Replace the image below with your dashboard screenshot.

```text
dashboard/dashboard_preview.png
```

or

```md
![Dashboard Preview](dashboard/dashboard_preview.png)
```

---

# Key Business Insights

The analysis reveals several important findings:

- SBI Mutual Fund manages the largest Assets Under Management (AUM) among all fund houses.
- SIP inflows show a steady upward trend, indicating increasing retail investor participation.
- Small Cap funds deliver the highest average 3-year returns compared to other categories.
- Equity funds account for the majority of overall fund allocation.
- Punjab records the highest investment volume among the analyzed states.
- Investors aged 26–35 represent the largest investor segment.
- Fund performance varies significantly across investment categories, emphasizing the importance of portfolio diversification.

---

# Project Outputs

The project successfully delivers:

- Cleaned datasets
- SQLite analytical database
- SQL analytical queries
- Data Dictionary
- Data Cleaning Report
- Data Quality Summary
- EDA Notebook
- Business Insights Report
- Power BI Dashboard
- Dashboard PDF

---

# How to Run

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/bluestock-mf-capstone.git
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

Repeat for the remaining cleaning scripts if needed.

---

## 4. Create SQLite Database

```bash
python scripts/load_to_db.py
```

---

## 5. Execute SQL Analysis

```bash
python scripts/run_query.py
```

---

## 6. Run Exploratory Data Analysis

Open:

```text
analysis/EDA.ipynb
```

Run all notebook cells to reproduce the analysis and figures.

---

## 7. Open Power BI Dashboard

Open the following file using Power BI Desktop:

```text
dashboard/Mutual_Fund_Dashboard.pbix
```

---

# Future Improvements

Possible future enhancements include:

- Predictive analytics for mutual fund performance
- Machine learning-based fund recommendation
- Automated ETL pipeline
- Real-time dashboard integration
- Deployment using Power BI Service

---

# Author

**Zalsabilah Rezky Amelia Arep**

Data Analyst Intern

Bluestock Fintech Capstone Project

---

# Acknowledgements

This project was developed as part of the **Bluestock Fintech Data Analyst Internship Capstone Program**, integrating data engineering, SQL analytics, exploratory data analysis, and business intelligence into a complete end-to-end analytics solution.