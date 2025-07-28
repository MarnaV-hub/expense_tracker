def add_expense(cursor, category, amount):
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, datetime('now'))", (category, amount))


def update_expense(cursor, expense_id, new_amount):
    cursor.execute("UPDATE expenses SET amount = ? WHERE id = ?", (new_amount, expense_id))


def delete_expense(cursor, expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))


def view_expenses(cursor):
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()


def view_expenses_by_category(cursor, category):
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    return cursor.fetchall()
