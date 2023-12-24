from uuid import uuid4
from datetime import datetime, timezone

class Expense:


    def __init__(self, title, amount):
        """ A method that takes the title and amount as parameters and sets the id, title, amount, created_at and updated_at attributes.
        """
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        """ A method that takes the title and amount as parameters and updates the title and amount attributes.If the update method is called without any parameters, the title and amount attributes remain unchanged. The updated_at attribute is updated to the current date and time in UTC.
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """ A method that returns a dictionary of the set of values inputted after the update method is called.
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
    
    def __repr__(self) -> str:
        return f"{self.title}_{self.amount}_{self.id} "

class ExpenseDatabase:

    
    def __init__(self):
        """ A method that initializes an empty list of expenses.
        """
        self.database = []



    def add_expense(self, expense):
        """ A method that takes an expense as a parameter and adds it to the list of expenses.
        """
        self.database.append(expense)
        print(f"{expense} added succesfully")
    

    def remove_expense(self, expense_id):
        """ A method that takes an expense_id as a parameter and removes the expense with the given id from the list of expenses.
        """
        for expense in self.database:
            if expense.id == expense_id:
                self.database.remove(expense)
                return self.database
                break
    

    def get_expense_by_id(self, expense_id):
        """ A method that takes an expense_id as a parameter and returns the expense with the given id.
        """
        for expense in self.database:
            if expense.id == expense_id:
                return expense
        return None


    def get_expense_by_title(self, expense_title):

        """ A method that takes an expense_title as a parameter and returns the expense with the given title.
        """
        matches = []
        for expense in self.database:
            if expense.title == expense_title:
                matches.append(expense)
        return matches

    def to_dict(self):
        """ A method that returns a copy of the list of expenses.
        """
        list_of_dicts =  [{
        'id': expense.id,
        'title': expense.title,
        'amount': expense.amount,
        'created_at': expense.created_at.strftime('%Y-%m-%d %H:%M:%S UTC'),
        'updated_at': expense.updated_at.strftime('%Y-%m-%d %H:%M:%S UTC')} for expense in self.database]

        dict_of_dicts = {item['id']: item for item in list_of_dicts}
        return dict_of_dicts
    

if __name__ == "__main__":
    expense_1 = Expense(title="fuel", amount=10000)
    expense_2 = Expense(title="transport", amount=2000)
    expense_3 = Expense(title="data", amount=1000)
    expense_4 = Expense(title="food", amount=3000)
    expense_5 = Expense(title="shoes", amount=10000)
    expense_6 = Expense(title="shoes", amount=300000)
    
    
    edb = ExpenseDatabase()
    
    # This part of the code add expense to the database 
    for expense in [expense_1, expense_2, expense_3, expense_4, expense_5, expense_6]:
        edb.add_expense(expense)
        print(edb.database)
        print()
        print("-"*30)
        print()

# Running the code to ensure it runs effectively. This update the expense_1
    print(expense_1.update(title="food", amount=5000))

# This part of the code remove expense from the ExpenseDatabase
    print(edb.remove_expense(expense_id=expense_2.id))

# This part of the code can fetch expense by id
    print(edb.get_expense_by_id(expense_id=expense_1.id))


# This part of the code can fetch expense by title
    print(edb.get_expense_by_title(expense_title="shoes"))

# This part of the code can return a dictionary of dictionaries for the ExpenseDatabase item
    print(edb.to_dict())