import csv
FILE_NAME = "expenses.csv"
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, Shopping, Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!\n")
def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        print("\nAll Expenses:")
        for row in reader:
            print(row)
        print()