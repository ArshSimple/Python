import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"D:\AA User File\Documents\GitHub\Python\sales.csv")
print("First 5 rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

total_revenue = df['Revenue'].sum()
print(f"\nTotal Revenue: ${total_revenue}")

revenue_by_product = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(revenue_by_product)

avg_quantity = df.groupby("Product")["Quantity"].mean()
print("\nAverage Quantity Sold per Product:")
print(avg_quantity)

df['Date'] = pd.to_datetime(df['Date'])
daily_revenue = df.groupby("Date")["Revenue"].sum()

output_excel = r"D:\AA User File\Documents\GitHub\Python\sales_analysis.xlsx"
with pd.ExcelWriter(output_excel) as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    revenue_by_product.to_frame(name="Revenue").to_excel(writer, sheet_name="Revenue by Product")
    avg_quantity.to_frame(name="Avg Quantity").to_excel(writer, sheet_name="Avg Quantity")
    daily_revenue.to_frame(name="Daily Revenue").to_excel(writer, sheet_name="Daily Revenue")
print(f"Analysis exported to {output_excel}")

img_dir = r"D:\AA User File\Documents\GitHub\Python"

plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind='bar', color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig(os.path.join(img_dir, "revenue_by_product.png"))
plt.close()

plt.figure(figsize=(10, 5))
daily_revenue.plot(marker='o', linestyle='-', color='green')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig(os.path.join(img_dir, "daily_revenue_trend.png"))
plt.close()

print("Charts saved as revenue_by_product.png and daily_revenue_trend.png")
