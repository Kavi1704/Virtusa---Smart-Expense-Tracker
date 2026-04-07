from expense_manager import add_expense, view_expenses
from report import monthly_summary
def menu():
    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary & Pie Chart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")
menu()