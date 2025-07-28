def set_financial_goal(cursor):
    description = input("Enter goal description: ")
    target_amount = float(input("Enter target amount: "))
    cursor.execute("INSERT INTO goals (description, target_amount) VALUES (?, ?)", (description, target_amount))
    print("Goal set successfully.")

def view_goal_progress(cursor):
    cursor.execute("SELECT * FROM goals")
    goals = cursor.fetchall()
    if not goals:
        print("No financial goals set.")
        return
    for goal in goals:
        print(f"Goal: {goal[1]}, Target: {goal[2]}, Saved: {goal[3]}, Remaining: {goal[2] - goal[3]}")