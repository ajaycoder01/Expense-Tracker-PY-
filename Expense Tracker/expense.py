# Question 1: Expense Tracker Using File Handling.

# 1. Add a new expense with: (Expense title | Category | Amount)
# 2. View all saved expenses.
# 3. Calculate and display the total expense.
# 4. Find and display the highest expense.
# 5. Search and display expenses by category.
# Store all expense records permanently in a file named expenses.txt.

FILE_NAME = "expenses.txt"


def add_expense():
    title = input("Enter expense title: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{title}|{category}|{amount}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.")
            return

        print("\n--- All Expenses ---")

        for expense in expenses:
            title, category, amount = expense.strip().split("|")

            print(
                f"Title: {title} | "
                f"Category: {category} | "
                f"Amount: ₹{float(amount):.2f}"
            )

    except FileNotFoundError:
        print("No expense file found.")


def calculate_total():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for expense in file:
                title, category, amount = expense.strip().split("|")
                total += float(amount)

        print(f"Total Expense: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


def highest_expense():
    highest = None

    try:
        with open(FILE_NAME, "r") as file:
            for expense in file:
                title, category, amount = expense.strip().split("|")
                amount = float(amount)

                if highest is None or amount > highest[2]:
                    highest = (title, category, amount)

        if highest:
            print("\n--- Highest Expense ---")
            print(f"Title: {highest[0]}")
            print(f"Category: {highest[1]}")
            print(f"Amount: ₹{highest[2]:.2f}")
        else:
            print("No expenses found.")

    except FileNotFoundError:
        print("No expenses found.")


def search_by_category():
    search_category = input("Enter category to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            print(f"\n--- Expenses in '{search_category}' ---")

            for expense in file:
                title, category, amount = expense.strip().split("|")

                if category.lower() == search_category:
                    print(
                        f"Title: {title} | "
                        f"Amount: ₹{float(amount):.2f}"
                    )
                    found = True

        if not found:
            print("No expenses found in this category.")

    except FileNotFoundError:
        print("No expenses found.")


def main():
    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expense")
        print("4. Find Highest Expense")
        print("5. Search Expense by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            highest_expense()

        elif choice == "5":
            search_by_category()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
