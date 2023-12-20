import uuid 
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        


class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
        

    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                self.expenses.remove(expense)
                break
    
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        return None


    def get_expense_by_title(self, expense_title):
        return [expense for expense in self.expenses if expense['title'] == expense_title]

    def to_dict(self):
        return self.expenses.copy()




IKenna = Expense()

print(Expense.name)
    