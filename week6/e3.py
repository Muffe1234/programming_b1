# Exercise 3: Personal Expense Tracker
# 1. Initialize Data Structures
# TODO: Create an empty list, `expense_records`, to store each expense as a tuple `(category, amount, date)`.
#Initialize an empty dictionary, `category_totals`, to sum spending by category.
#Initialize an empty set, `unique_categories`, to track all distinct categories.
expense_records = [
    ("Food", 100.00, "2026-01-01"),
    ("Food", 50.00, "2026-01-02"),
    ("Utilities", 150.00, "2026-01-03"),
    ("Entertainment", 75.00, "2026-01-04"),
    ("Other", 25.00, "2026-01-05"),
]
category_totals = {}
unique_categories = set()



# 2. Collect Expense Data
# TODO: Implement a loop to prompt the user for 5-7 individual expenses.
#For each expense, collect the category (e.g., "Food", "Transport", "Utilities"),
#the amount (float), and the date (string, e.g., "YYYY-MM-DD").
#Store each expense as a tuple in `expense_records`.
# Example:

def add_expense():
    category = input(f"Enter expense category: ")
    amount = float(input(f"Enter expense amount: "))
    date = input(f"Enter expense date (YYYY-MM-DD): ")
    expense_records.append((category, amount, date))
    print("Expense added successfully")
# 3. Categorize and Sum Expenses
# TODO: Iterate through `expense_records`.
#For each expense, add its category to `unique_categories`.
#Update the running total for that category in `category_totals`.
#If a category doesn't exist yet in the dictionary, initialize it.

def categorize_and_sum_expenses():
    for category, amount, date in expense_records:
        unique_categories.add(category)
        category_totals[category] = category_totals.get(category, 0) + amount



# Example:
# for category, amount, date in expense_records:
#unique_categories.add(category)
#category_totals[category] = category_totals.get(category, 0) + amount


# 4. Calculate Overall Statistics
# TODO: Extract all expense amounts into a separate list.
#Compute the `total_spending`, `average_expense`, `highest_expense`, and `lowest_expense`.
#Store these statistics in a separate dictionary, e.g., `overall_stats`.


    
# Example:
# all_amounts = [amount for category, amount, date in expense_records]
# total_spending = sum(all_amounts)
# average_expense = total_spending / len(all_amounts) if all_amounts else 0
# highest_expense = max(all_amounts) if all_amounts else 0
# lowest_expense = min(all_amounts) if all_amounts else 0
# To find highest/lowest expense with category/date:
# highest_expense_record = max(expense_records, key=lambda x: x[1]) if expense_records else None
# lowest_expense_record = min(expense_records, key=lambda x: x[1]) if expense_records else None




# 5. Generate Spending Report
# TODO: Print a comprehensive report.
#Start with a header for "Overall Spending Summary," displaying total spending,
#average expense, and highest/lowest expense.
#Follow with "Unique Categories Spent On" (using the set).
#Finally, present "Spending by Category," iterating through `category_totals`
#and showing each category's name and total spending.
#Ensure clear formatting and appropriate currency symbols (e.g., "$").
# Example:
# print("\n=== OVERALL SPENDING SUMMARY ===")
# print(f"Total Spending: ${total_spending:.2f}")
# print(f"Average Expense: ${average_expense:.2f}")
# if highest_expense_record:
#print(f"Highest Expense: ${highest_expense_record[1]:.2f} (Category: {highest_expense_record[0]}, Date: {highest_expense_record[2]})")
# if lowest_expense_record:
#print(f"Lowest Expense: ${lowest_expense_record[1]:.2f} (Category: {lowest_expense_record[0]}, Date: {lowest_expense_record[2]})")
# print("\n=== UNIQUE CATEGORIES SPENT ON ===")
# print(unique_categories)
# print(f"Total unique categories: {len(unique_categories)}")
# print("\n=== SPENDING BY CATEGORY ===")
# for category, total in category_totals.items():
#print(f"{category}: ${total:.2f}")
def print_summary():
    all_amounts = [amount for category, amount, date in expense_records]
    total_spending = sum(all_amounts)
    average_expense = total_spending / len(all_amounts)
    highest_expense = max(all_amounts)
    lowest_expense = min(all_amounts)
    highest_expense_record = max(expense_records, key=lambda x: x[1])
    lowest_expense_record = min(expense_records, key=lambda x: x[1])
    print("\n=== OVERALL SPENDING SUMMARY ===")
    print(f"Total Spending: ${total_spending:.2f}")
    print(f"Average Expense: ${average_expense:.2f}")
    print(f"Highest Expense: ${highest_expense_record[1]:.2f} (Category: {highest_expense_record[0]}, Date: {highest_expense_record[2]})")
    print(f"Lowest Expense: ${lowest_expense_record[1]:.2f} (Category: {lowest_expense_record[0]}, Date: {lowest_expense_record[2]})")
    print("\n=== UNIQUE CATEGORIES SPENT ON ===")
    print(unique_categories)
    print(f"Total unique categories: {len(unique_categories)}")
    print("\n=== SPENDING BY CATEGORY ===")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


while True:
    print("Menu:")
    print("1. Add a new expense")
    print("2. Print summary")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        categorize_and_sum_expenses()
        print_summary()
    elif choice == '3': 
        break