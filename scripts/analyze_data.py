import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Connect
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='indian_stocks'
)

# Query
query = "SELECT trade_date, close_price FROM stocks WHERE ticker='INFY';"
df = pd.read_sql(query, conn)
df['trade_date'] = pd.to_datetime(df['trade_date'])
df = df.sort_values('trade_date')

# Stats
print(f"Mean Close: {df['close_price'].mean():.2f}")
print(f"Median Close: {df['close_price'].median():.2f}")
print(f"Mode Close: {df['close_price'].mode()[0]:.2f}")
print(f"Volatility (std dev): {df['close_price'].std():.2f}")

# Daily returns
df['daily_return'] = df['close_price'].pct_change()

# Price trend
plt.figure(figsize=(10,6))
plt.plot(df['trade_date'], df['close_price'], color='blue')
plt.title('INFY Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.savefig('visuals/price_trend.png')

# Returns dist
plt.figure(figsize=(10,6))
sns.histplot(df['daily_return'].dropna(), kde=True, bins=50)
plt.title('INFY Daily Returns Distribution')
plt.savefig('visuals/daily_returns.png')

print("✅ Analysis & visuals done.")
