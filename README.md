# 🇮🇳 Indian Stock Market Analysis & Reporting System

## 📈 Overview
Analyze historical stock prices for Indian companies (NSE/BSE) using Python and MySQL. Store raw data, clean & analyze it, generate descriptive stats, and create clear visual reports.

## ⚙️ Tech Stack
- **Languages:** Python, SQL
- **Database:** MySQL
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, mysql-connector-python

## 🚀 Features
- Load raw stock CSV data into MySQL
- Run EDA: mean, median, mode, volatility, daily returns
- Visualize price trends and return distributions
- Export summary stats to CSV
- Store visuals for presentation

## 🧩 How to Run
1. Clone repo  
2. Create MySQL DB: `CREATE DATABASE indian_stocks;`  
3. Run `create_tables.sql` to create tables  
4. Place `raw_stock_data.csv` in `/data`  
5. Install dependencies: `pip install -r requirements.txt`  
6. Run scripts in order:
   - `load_data.py`
   - `analyze_data.py`
   - `generate_report.py`

## 📃 License
Educational / Demo Use Only
