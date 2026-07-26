# 📊 Vendor Performance Analysis

## 📌 Overview

Vendor Performance Analysis is an end-to-end data analytics project that evaluates vendor, brand, sales, purchasing, and inventory performance using **Python, SQL (SQLite), and Power BI**.

The project follows a complete analytics workflow—from ingesting raw data into a database, preparing a consolidated analytical dataset, performing exploratory data analysis (EDA), answering business research questions, conducting statistical analysis, and building an interactive Power BI dashboard.

---

# 🎯 Business Objectives

This project aims to help businesses make informed procurement and inventory decisions by:

* Evaluating vendor performance.
* Identifying top-performing vendors and brands.
* Analyzing procurement patterns.
* Measuring inventory efficiency.
* Evaluating profitability.
* Generating actionable business recommendations.

---

# 🛠️ Tech Stack

| Category       | Tools               |
| -------------- | ------------------- |
| Programming    | Python              |
| Data Analysis  | Pandas, NumPy       |
| Database       | SQLite              |
| Query Language | SQL                 |
| Visualization  | Matplotlib, Seaborn |
| Dashboard      | Power BI            |
| Environment    | Jupyter Notebook    |

---

# 📂 Repository Structure

```text
VENDOR-PERFORMANCE-ANALYSIS/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── notebook/
│   ├── EDA.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
│
├── Dashboard/
│   └── vendor_performance.pbix
│
├── Images/
│   └── dashboard.png
│
└── Report/
    └── Vendor Performance Report.pdf
    
```

---

# 🔄 Project Workflow

```text
Raw CSV Files
        │
        ▼
Data Ingestion
(ingestion_db.py)
        │
        ▼
SQLite Database
(inventory.db)
        │
        ▼
Vendor Summary Generation
(get_vendor_summary.py)
        │
        ▼
vendor_sales_summary
        │
        ├──────────────► EDA.ipynb
        │
        ▼
vendor_performance_analysis.ipynb
        │
        ▼
Business Insights
        │
        ▼
Power BI Dashboard
```

---

# ⚙️ Project Components

### 📄 `scripts/ingestion_db.py`

* Reads raw CSV files.
* Loads datasets into a SQLite database.
* Creates database tables automatically.
* Logs the ingestion process.

### 📄 `scripts/get_vendor_summary.py`

* Combines multiple database tables.
* Creates the consolidated `vendor_sales_summary` table.
* Generates the analytical dataset used throughout the project.

### Logging

Both data processing scripts generate log files during execution to track progress, execution time, and errors.

- `ingestion_db.py` → Generates `ingestion_db.log`
- `get_vendor_summary.py` → Generates `get_vendor_summary.log`

> Note: Log files are excluded from version control using `.gitignore`.

### 📓 `notebooks/EDA.ipynb`

* Database exploration
* Data quality assessment
* Missing value analysis
* Duplicate detection
* Outlier analysis
* Exploratory Data Analysis (EDA)

### 📓 `notebooks/vendor_performance_analysis.ipynb`

* Feature engineering
* Vendor performance analysis
* Sales and profitability analysis
* Inventory analysis
* Statistical analysis
* Research question analysis
* Business insights

### 📊 `dashboard/vendor_performance_dashboard.pbix`

Interactive Power BI dashboard for exploring vendor performance through KPIs and visualizations.

---

# 🧹 Data Preparation

The following preprocessing steps were performed:

* Loaded multiple CSV files into SQLite.
* Combined purchase, sales, inventory, and vendor datasets.
* Removed duplicate records.
* Handled missing values.
* Corrected data types.
* Identified outliers using the IQR method.
* Created derived business metrics.

---

# 📈 Key Performance Indicators (KPIs)

The analysis focuses on the following KPIs:

* Total Sales Revenue
* Total Purchase Value
* Gross Profit
* Profit Margin (%)
* Sales Quantity
* Purchase Quantity
* Average Purchase Price
* Average Selling Price
* Stock Turnover Ratio
* Unsold Inventory Value
* Freight Cost
* Vendor Purchase Contribution (%)
* Vendor Sales Contribution (%)

---

# 🔧 Feature Engineering

The following business metrics were created:

* Gross Profit
* Profit Margin
* Stock Turnover
* Purchase Contribution
* Sales Contribution
* Inventory Value

These metrics were used to evaluate vendor profitability, inventory efficiency, and procurement performance.

---

# ❓ Research Questions

This project answers the following business questions:

1. Identify brands that require promotional or pricing adjustments due to lower sales performance but higher profit margins.
2. Which vendor and brand demonstrate the highest sales performance?
3. Which vendor contributes the most to the total purchase value?
4. How much of the total procurement is dependent on the top vendors?
5. Does purchasing in bulk reduce the unit purchase price? What is the optimal purchase volume for cost savings?
6. Which vendors have low inventory turnover, indicating excess stock and slow-moving products?
7. How much capital is locked in unsold inventory for each vendor, and which vendors contribute the most to it?
8. What are the 95% confidence intervals for the profit margins of top-performing and low-performing vendors?

---

# 📊 Exploratory Data Analysis

The project includes:

* Summary Statistics
* Missing Value Analysis
* Duplicate Analysis
* Outlier Detection
* Distribution Analysis
* Vendor Analysis
* Brand Analysis
* Sales Analysis
* Purchase Analysis
* Inventory Analysis
* Correlation Analysis
* Statistical Analysis

---

# 💡 Key Insights

* A small number of vendors contribute a significant share of total procurement and sales.
* Several brands have high profit margins but relatively low sales, making them strong candidates for targeted promotions or pricing adjustments.
* Bulk purchasing can reduce unit purchase costs beyond certain order quantities, improving procurement efficiency.
* Some vendors exhibit low inventory turnover, indicating excess stock and slow-moving products.
* A considerable amount of capital is tied up in unsold inventory, highlighting opportunities for inventory optimization.
* Freight costs vary significantly across vendors and influence overall procurement costs.

---

# ✅ Final Recommendations

* Diversify the vendor base to reduce procurement risk and avoid over-dependence on a small number of suppliers.
* Optimize bulk purchasing strategies by identifying the purchase volume that minimizes unit costs while avoiding excess inventory.
* Review pricing and promotional strategies for slow-moving, high-margin brands to improve sales while maintaining profitability.
* Reduce capital tied up in unsold inventory through targeted promotions, discounts, or inventory rationalization.
* Strengthen marketing efforts for underperforming vendors by improving product visibility or reassessing vendor partnerships.

---

# 📊 Dashboard

The Power BI dashboard provides interactive insights into:

* Executive KPIs
* Vendor Performance
* Brand Performance
* Sales Analysis
* Purchase Analysis
* Inventory Analysis
* Profitability Analysis
* Stock Turnover
* Freight Cost Analysis

### Dashboard Preview

> Replace the filename below with your actual dashboard image if it differs.

```markdown
![Vendor Performance Dashboard](images/dashboard.png)
```

---

# 📄 Project Report

A detailed report containing the complete methodology, analysis, visualizations, statistical findings, business insights, and recommendations is available in:

```text
reports/Vendor_Performance_Report.pdf
```

---

# 🚀 How to Run the Project

### Clone the repository

```bash
git clone https://github.com/srijitaaa2005/VENDOR-PERFORMANCE-ANALYSIS.git
```


### Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy scipy jupyter
```

### Load the data into SQLite

```bash
python scripts/ingestion_db.py
```

### Generate the analytical dataset

```bash
python scripts/get_vendor_summary.py
```

### Run the notebooks

Execute the notebooks in the following order:

1. `EDA.ipynb`
2. `vendor_performance_analysis.ipynb`

### Open the Power BI Dashboard

Open the `.pbix` file located in the `dashboard/` folder using Microsoft Power BI Desktop.

---


# 🔮 Future Enhancements

* Automate data refresh for new datasets.
* Expand the dashboard with additional KPIs and drill-through reports.
* Develop predictive models for sales and demand forecasting.
* Publish the dashboard using Power BI Service.

---



