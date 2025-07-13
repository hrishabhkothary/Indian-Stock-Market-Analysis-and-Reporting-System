import pandas as pd
import mysql.connector

# Connect
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='indian_stocks'
)
cursor = conn.cursor()

# Load CSV
df = pd.read_csv('data/raw_stock_data.csv')

# Clean
df = df.dropna()
df['trade_date'] = pd.to_datetime(df['trade_date'])

# Insert
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO stocks (ticker, trade_date, open_price, high_price, low_price, close_price, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['ticker'],
        row['trade_date'],
        row['open'],
        row['high'],
        row['low'],
        row['close'],
        row['volume']
    ))

conn.commit()
print("✅ Data loaded successfully.")
conn.close()
