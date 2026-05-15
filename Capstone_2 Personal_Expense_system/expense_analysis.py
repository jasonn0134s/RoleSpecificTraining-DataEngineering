import pandas as pd
import numpy as np

df = pd.read_csv("expenses.csv")

df['amount'] = df['amount'].astype(float)

df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.to_period('M')

total_expense = np.sum(df['amount'])

average_expense = np.mean(df['amount'])

print("Total Expense:", total_expense)

print("Average Expense:", average_expense)

category_summary = df.groupby('category')['amount'].sum()

print("\nCategory Wise Expense Summary")

print(category_summary)

monthly_summary = df.groupby(['month', 'category'])['amount'] \
    .sum() \
    .unstack() \
    .fillna(0)

print("\nMonthly Expense Summary")

print(monthly_summary)