# List to store expense data
expenses = []

# Add expense
def add_expense(category, amount, date):
    expense = {"category": category, "amount": amount, "date": date}
    expenses.append(expense)
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded bro.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']} - Date: {expense['date']} - Amount: ${expense['amount']:.2f}")
    
# Filter by category
def filter_categorized_expenses(category):
    filtered_expenses = [expense for expense in expenses if expense["category"] == category]
    
    if filtered_expenses:
        for i, expense in enumerate(filtered_expenses, start=1):
            print(f"{i}. Category: {expense['category']} - Date: {expense['date']} - Amount: ${expense['amount']:.2f}")
    else:
        print(f"No expenses found for category: {category}")
            
# Calculate total expenses
def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

# Delete expense by index (1-based)
def delete_expense(index):
    try:
        removed_expense = expenses.pop(index - 1)
        print(f"Deleted Expense: {removed_expense['category']} on {removed_expense['date']} - ${removed_expense['amount']:.2f}")
    except IndexError:
        print("Invalid index bro.")

# Main menu
def main():
    while True:
        print("\nExpense Tracker:┬┴┬┴┤(･_├┬┴┬┴")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Calculate Total")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category bro: ")
            try:
                amount = float(input("Enter amount bro: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            date = input("Enter date bro (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Enter category bro: ")
            filter_expenses_by_category(category)
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            try:
                index = int(input("Enter expense index to delete bro: "))
            except ValueError:
                print("Invalid index. Please enter a number.")
                continue
            delete_expense(index)
        elif choice == "6":
            print("lol bye (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
