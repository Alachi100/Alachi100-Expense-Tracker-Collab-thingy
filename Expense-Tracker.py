# Dictionary to store expense data
expenses = []
# Add expenses
def add_expense(category, amount, date):
    expense = {"category": category, "amount": amount, "date": date}
    expenses.append(expense)
# View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
# Group and filter expenses by category
def categorized_expenses():
    for expense in expenses:
        category = expense["category"]
        if category not in categorized_expenses:
            categorized_expenses[category] = []
        categorized_expenses[category].append(expense)
    
    for category, expenses_list in categorized_expenses.items():
        print(f"\nCategory: {category}")
        for i, expense in enumerate(expenses_list, start=1):
            print(f"{i}. Date: {expense['date']} - Amount: ${expense['amount']:.2f}")
# Calculating total expense
def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")
# Delete expense
def delete_expense(index):
    try:
        removed_expense = expenses.pop(index - 1)
        print(f"Deleted Expense: {removed_expense['category']} on {removed_expense['date']} - ${removed_expense['amount']:.2f}")
    except IndexError:
        print("Invalid index. No expense found at that index.")

# Menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Calculate Total")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Enter category to filter: ")
            filter_expenses_by_category(category)
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            index = int(input("Enter expense index to delete: "))
            delete_expense(index)
        elif choice == "6":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
