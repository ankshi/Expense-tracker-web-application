import matplotlib.pyplot as plt

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)

    def generate_summary(self):
        category_totals = {}
        total_expenses = 0

        for expense in self.expenses:
            total_expenses += expense.amount
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount

        print("Expense Summary:")
        print("-" * 30)
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
        print("-" * 30)
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        # Generate and show pie chart
        self.generate_pie_chart(category_totals)

    def generate_pie_chart(self, category_totals):
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title("Expense Categories Distribution")
        plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
        plt.show()


# Create an instance of the ExpenseManager
expense_manager = ExpenseManager()

# Adding expenses
expense_manager.add_expense("Groceries", 50.00, "Food")
expense_manager.add_expense("Gasoline", 30.00, "Transportation")
expense_manager.add_expense("Dinner", 60.00, "Food")
expense_manager.add_expense("Movie", 15.00, "Entertainment")

# Generating and displaying the summary and visualization
expense_manager.generate_summary()
