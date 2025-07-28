def add_income():
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    date = input("Enter income date (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO income (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    print("Income added successfully.")

def view_income():
    cursor.execute("SELECT * FROM income")
    for row in cursor.fetchall():
        print(row)

def view_income_by_category():
    category = input("Enter category: ")
    cursor.execute("SELECT * FROM income WHERE category = ?", (category,))
    for row in cursor.fetchall():
        print(row)

def delete_income_category():
    category = input("Enter income category to delete: ")
    cursor.execute("DELETE FROM income WHERE category = ?", (category,))
    conn.commit()
    print("Income category deleted successfully.")

def update_income_amount():
    category = input("Enter income category to update: ")
    new_amount = float(input("Enter new income amount: "))
    cursor.execute("UPDATE income SET amount = ? WHERE category = ?", (new_amount, category))
    conn.commit()
    print("Income amount updated successfully.")