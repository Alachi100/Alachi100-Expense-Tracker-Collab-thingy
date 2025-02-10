# Dictionary to store expense data
expenses = []
# Add expenses
def add_expense(category, amount, date):
    expense = {"category bro": category, "amount bro": amount, "date bro": date}
    expenses.append(expense)
# View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded bro.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']} - Date: {expense['date']} - Amount: ${expense['amount']:.2f}")
#filtering expense
def filter_expenses_by_category():
    for expense in expenses:
    category = expense("category")
elif category not 
# Calculating total
def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")
# Delete expense
def delete_expense(index):
    try:
        removed_expense = expenses.pop(index - 1)
        print(f"Deleted Expense: {removed_expense['category']} on {removed_expense['date']} - ${removed_expense['amount']:.2f}")
    except IndexError:
        print("Invalid index bro")

# Menu
def main():
    while True:
        print("Expense Tracker:┬┴┬┴┤(･_├┬┴┬┴")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Calculate Total")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category bro: ")
            amount = float(input("Enter amount bro: "))
            date = input("Enter date bro(YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Enter category bro: ")
            filter_expenses_by_category()
        elif choice == "4":
            calculate_total_expenses()
        elif choice == "5":
            index = int(input("Enter expense to delete bro "))
            delete_expense(index)
        elif choice == "6":
            print("lol bye(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
