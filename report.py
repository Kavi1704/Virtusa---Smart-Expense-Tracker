import csv
import matplotlib.pyplot as plt
from collections import defaultdict
FILE_NAME = "expenses.csv"
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    category_totals = defaultdict(float)
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['date'].startswith(month):
                amount = float(row['amount'])
                category = row['category']
                total += amount
                category_totals[category] += amount
    print("\n===== Monthly Expense Summary =====")
    print("Total Expenses:", total)
    print("\nCategory-wise Breakdown:")
    for cat, amt in category_totals.items():
        print(cat, ":", amt)
    if category_totals:
        highest = max(category_totals, key=category_totals.get)
        print("\nHighest Spending Category:", highest)
        plt.pie(
            category_totals.values(),
            labels=category_totals.keys(),
            autopct='%1.1f%%'
        )
        plt.title("Expense Distribution - " + month)
        plt.show()
    else:
        print("No expenses found for this month.")