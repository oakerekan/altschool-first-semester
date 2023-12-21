import uuid 
from datetime import datetime, timezone

class Expense:
    """ A class representing a single expense, with its title, amount, created_at and updated_at. The id is generated automatically using the uuid library.
    The created_at and updated_at are generated automatically using the datetime library and contain the current date and time in UTC. The Class expense 
    contain an __init__ method that takes the title and amount as parameters and sets the id, title, amount, created_at and updated_at attributes. 
    also contain an update method that takes the title and amount as parameters and updates the title and amount attributes. The to_dict method returns a  dictionary of the set of values inputted after the update method is called.   
    """

    def __init__(self, title, amount):
        """ A method that takes the title and amount as parameters and sets the id, title, amount, created_at and updated_at attributes."""
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        """ A method that takes the title and amount as parameters and updates the title and amount attributes.If the update method is called without any parameters, the title and amount attributes remain unchanged. The updated_at attribute is updated to the current date and time in UTC."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """ A method that returns a dictionary of the set of values inputted after the update method is called."""
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        


class ExpenseDatabase:

    """ A class representing a collection of expenses. The class contains an __init__ method that initializes an empty list of expenses.The class also contains an add_expense method that takes an expense as a parameter and adds it to the list of expenses. It also contains an remove_expense method that takes an expense_id as a parameter and removes the expense with the given id from the list of expenses. The get_expense_by_id method takes an expense_id as a parameter and returns the expense with the given id. Also, the get_expense_by_title method takes an expense_title as a parameter and returns the expense with the given title. The to_dict method returns a copy of the list of expenses.
    """
    def __init__(self):
        """ A method that initializes an empty list of expenses."""
        self.expenses = []
        

    def add_expense(self, expense):
        """ A method that takes an expense as a parameter and adds it to the list of expenses."""
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        """ A method that takes an expense_id as a parameter and removes the expense with the given id from the list of expenses."""
        for expense in self.expenses:
            if expense['id'] == expense_id:
                self.expenses.remove(expense)
                break
    
    def get_expense_by_id(self, expense_id):
        """ A method that takes an expense_id as a parameter and returns the expense with the given id."""
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        return None


    def get_expense_by_title(self, expense_title):
        """ A method that takes an expense_title as a parameter and returns the expense with the given title."""
        return [expense for expense in self.expenses if expense['title'] == expense_title]

    def to_dict(self):
        """ A method that returns a copy of the list of expenses."""
        return self.expenses.copy()