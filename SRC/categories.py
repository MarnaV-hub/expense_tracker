def add_expense_category(cursor, category):
    cursor.execute("INSERT INTO expense_categories (category) VALUES (?)", (category,))
    print(f"Expense category '{category}' added successfully.")


def delete_expense_category(cursor, category):
    cursor.execute("DELETE FROM expense_categories WHERE category = ?", (category,))
    print(f"Expense category '{category}' deleted successfully.")


def view_expense_categories(cursor):
    cursor.execute("SELECT * FROM expense_categories")
    categories = cursor.fetchall()
    if categories:
        print("Expense Categories:")
        for category in categories:
            print(f"- {category[0]}")
    else:
        print("No expense categories found.")


def add_income_category(cursor, category):
    cursor.execute("INSERT INTO income_categories (category) VALUES (?)", (category,))
    print(f"Income category '{category}' added successfully.")


def delete_income_category(cursor, category):
    cursor.execute("DELETE FROM income_categories WHERE category = ?", (category,))
    print(f"Income category '{category}' deleted successfully.")


def view_income_categories(cursor):
    cursor.execute("SELECT * FROM income_categories")
    categories = cursor.fetchall()
    if categories:
        print("Income Categories:")
        for category in categories:
            print(f"- {category[0]}")
    else:
        print("No income categories found.")
