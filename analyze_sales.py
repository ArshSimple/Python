import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("sales.csv")

# Show the first few rows
print("📊 First 5 rows:")
print(df.head())

# Basic stats
print("\n📈 Summary Statistics:")
print(df.describe())

# Total revenue
total_revenue = df['Revenue'].sum()
print(f"\n💰 Total Revenue: ${total_revenue}")

# Revenue per product
revenue_by_product = df.groupby("Product")["Revenue"].sum()
print("\n📦 Revenue by Product:")
print(revenue_by_product)

# Plot revenue per product
plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind='bar', color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Quantity analysis
avg_quantity = df.groupby("Product")["Quantity"].mean()
print("\n📊 Average Quantity Sold per Product:")
print(avg_quantity)

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Daily revenue trend
daily_revenue = df.groupby("Date")["Revenue"].sum()
daily_revenue.plot(marker='o', linestyle='-', color='green')
plt.title("📅 Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
