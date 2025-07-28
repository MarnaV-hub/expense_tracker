# Expense Tracker

This is an expense and budget tracking application that allows users to monitor their spending, create expense categories, view spending summaries by category, and track their budget by calculating remaining funds based on their income and expenses.

## Features

- Add new expense categories to the database
- Update expense amounts
- Delete expense categories from the database
- Track spending
- Add income and income categories
- Delete income categories from the database
- Track income
- View expense or income categories
- Calculate the user’s budget based on the provided income and expenses

## Project Structure

```
expense_tracker
├── src
│   ├── main.py          # Entry point of the application
│   ├── database.py      # Manages database connection and operations
│   ├── expenses.py      # Functions related to expense management
│   ├── income.py        # Functions related to income management
│   ├── categories.py     # Manages expense and income categories
│   ├── budget.py        # Functions to manage budgets
│   └── goals.py         # Manages financial goals
├── requirements.txt     # Lists project dependencies
└── README.txt            # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd expense_tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

Follow the on-screen menu to manage your expenses, income, budgets, and financial goals.

## License

This project is licensed under the MIT License.
