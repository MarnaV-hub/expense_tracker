def set_budget(cursor, category, amount):
    cursor.execute("REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
    print("Budget set successfully.")


def view_budget(cursor, category):
    cursor.execute("SELECT amount FROM budgets WHERE category = ?", (category,))
    result = cursor.fetchone()
    if result:
        budget_amount = result[0]
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))
        total_spent = cursor.fetchone()[0] or 0
        print(f"Budget for {category}: {budget_amount}, Spent: {total_spent}, Remaining: {budget_amount - total_spent}")
    else:
        print("No budget set for this category.")


def calculate_remaining_budget(cursor, category):
    cursor.execute("SELECT amount FROM budgets WHERE category = ?", (category,))
    budget = cursor.fetchone()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))
    total_spent = cursor.fetchone()[0] or 0
    if budget:
        remaining = budget[0] - total_spent
        return remaining
    return None
