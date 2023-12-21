<h1>Building an Expense Tracker in Python using Python OOP.</h1>

This project intends to build an expense tracker using python object-oriented programming concepts. 

In this project we created two classes: "Expense" and "ExpenseDatabase"

<h2>Expense Class</h2>
Have methods such as __init__, update and to_dict.

Methods:

__init__(self, title, amount): Initializes an Expense object with a unique ID, title, amount, creation time, and update time.
update(self, title=None, amount=None): Updates the title and/or amount of the expense and modifies the updated_at timestamp accordingly.
to_dict(self): Converts the expense object into a dictionary format for easy serialization.

<h2>ExpenseDatabase Class</h2>

Have methods such as __init__, add_expense, remove_expense, get_expense_by_id, get expense_by_title, to_dict

Methods:
__init__(self): Initializes an empty list to store expenses.
add_expense(self, expense): Adds a new expense object to the database.
remove_expense(self, expense_id): Removes an expense from the database by its ID.
get_expense_by_id(self, expense_id): Retrieves an expense by its ID.
get_expense_by_title(self, expense_title): Retrieves a list of expenses with a given title.
to_dict(self): Converts the list of expenses into a dictionary format for easy serialization.


<h2>Notes</h2>
The Expense class represents individual expenses with unique IDs, titles, amounts, creation times, and update times.
The ExpenseDatabase class manages a list of expenses, allowing addition, removal, and retrieval based on ID or title.
The code uses UUID for unique identification, datetime for timestamp management, and dictionary formats for easy conversion and serialization.