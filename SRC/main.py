import sqlite3
from database import Database
from expenses import Expenses
from income import Income
from budget import Budget
from goals import Goals

def main():
    db = Database('budget_tracker.db')
    expenses = Expenses(db)
    income = Income(db)
    budget = Budget(db)
    goals = Goals(db)

    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View expenses by category")
        print("4. Add income")
        print("5. View income")
        print("6. View income by category")
        print("7. Set budget for a category")
        print("8. View budget for a category")
        print("9. Set financial goals")
        print("10. View progress towards financial goals")
        print("11. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            expenses.add_expense()
        elif choice == '2':
            expenses.view_expenses()
        elif choice == '3':
            expenses.view_expenses_by_category()
        elif choice == '4':
            income.add_income()
        elif choice == '5':
            income.view_income()
        elif choice == '6':
            income.view_income_by_category()
        elif choice == '7':
            budget.set_budget()
        elif choice == '8':
            budget.view_budget()
        elif choice == '9':
            goals.set_financial_goal()
        elif choice == '10':
            goals.view_goal_progress()
        elif choice == '11':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    db.close()

if __name__ == '__main__':
    main()
