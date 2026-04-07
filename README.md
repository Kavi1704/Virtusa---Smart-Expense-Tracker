Smart Expense Tracker 

About the Project

This is a simple command-line based Expense Tracker built using Python.
The main idea behind this project is to help users record their daily expenses and understand where their money is being spent.

Instead of using complex tools or apps, this project uses a basic CSV file to store data and provides a simple menu to interact with it.

 What This Project Does

* Allows users to add daily expenses (date, category, amount, description)
* Stores all data in a CSV file
* Displays all recorded expenses
* Generates a monthly summary of expenses
* Shows category-wise spending
* Identifies the highest spending category
* Displays a pie chart for better visualization

 Technologies Used

* Python
* CSV (for data storage)
* Matplotlib (for pie chart visualization)

 Project Structure

SmartExpenseTracker/
│
├── main.py                → Handles menu and program flow
├── expense_manager.py    → Handles adding and viewing expenses
├── report.py             → Generates summary and pie chart
├── expenses.csv          → Stores all expense data
└── README.md             → Project documentation

 How to Run the Project

 Step 1: Install Required Library

```bash
pip install matplotlib
```

 Step 2: Run the Program

```bash
python main.py
```

 Sample Data (expenses.csv)


date,category,amount,description
2026-04-06,Food,120.0,lunch
2026-03-01,Food,500.0,burger and pizza
2025-05-09,Shopping,1000.0,"cosmetic,dress"
2025-09-07,Travel,1500.0,went to trip


 How the Program Works

1. The program starts with a menu:

   * Add Expense
   * View Expenses
   * Monthly Summary
   * Exit

2. When adding an expense:

   * User enters date, category, amount, and description
   * Data is stored in `expenses.csv`

3. When viewing expenses:

   * All stored records are displayed

4. When generating monthly summary:

   * User enters a month (example: 2026-04)
   * Program filters data for that month
   * Calculates:

     * Total expenses
     * Category-wise totals
     * Highest spending category
   * Displays a pie chart



 Output Features

Monthly Summary

Displays total expenses for the selected month.

 Category-wise Breakdown

Shows how much is spent in each category.

 Highest Spending Category

Identifies which category has the highest expense.

 Pie Chart

A visual representation of spending using matplotlib.
 Concepts Used

* File Handling (CSV)
* Functions
* Loops and Conditions
* Dictionary (defaultdict)
* Data processing
* Visualization using matplotlib
* CLI-based program structure

 Why I Built This

I created this project to practice Python concepts like file handling, data processing, and visualization.
It also helped me understand how real-world applications track and analyze data.

Author

Kavibharathi M
