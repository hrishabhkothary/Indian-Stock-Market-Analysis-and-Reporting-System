import pandas as pd
import mysql.connector

# Connect
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='indian_stocks'
)

# Query
query = "SELECT * FROM stocks WHERE ticker='INFY';"
df = pd.read_sql(query, conn)

summary = {
    'Mean_Close': df['close_price'].mean(),
    'Median_Close': df['close_price'].median(),
    'Mode_Close': df['close_price'].mode()[0],
    'Volatility': df['close_price'].std(),
    'Max_Close': df['close_price'].max(),
    'Min_Close': df['close_price'].min()
}

report_df = pd.DataFrame([summary])
report_df.to_csv('data/summary_report.csv', index=False)
print("✅ Summary report generated: data/summary_report.csv")
