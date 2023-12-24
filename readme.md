<h1>1.0 Building an Expense Tracker in Python using Object Oriented Programming.</h1>

This project intends to build an expense tracker using python object-oriented programming concepts. 

In this project we created two classes: "Expense" and "ExpenseDatabase"

<h2>Expense Class</h2>
Have methods such as __init__, update and to_dict.

Methods:

**__init__(self, title, amount)**: Initializes an Expense object with a unique ID, title, amount, creation time, and update time.<br>
**update(self, title=None, amount=None)**: Updates the title and/or amount of the expense and modifies the updated_at timestamp accordingly.<br>
**to_dict(self)**: Converts the expense object into a dictionary format for easy serialization.<br>

<h2>ExpenseDatabase Class</h2>

Have methods such as __init__, add_expense, remove_expense, get_expense_by_id, get expense_by_title, to_dict

Methods:

__init__(self): Initializes an empty list to store expenses.<br>
**add_expense(self, expense)**: Adds a new expense object to the database.<br>
**remove_expense(self, expense_id)**: Removes an expense from the database by its ID.<br>
**get_expense_by_id(self, expense_id)**: Retrieves an expense by its ID.<br>
**get_expense_by_title(self, expense_title)**: Retrieves a list of expenses with a given title.<br>
**to_dict(self)**: Converts the list of expenses into a dictionary format for easy serialization.<br>


<h2>Notes</h2>
The Expense class represents individual expenses with unique IDs, titles, amounts, creation times, and update times.<br>
The ExpenseDatabase class manages a list of expenses, allowing addition, removal, and retrieval based on ID or title.<br>
The code uses UUID for unique identification, datetime for timestamp management, and dictionary formats for easy conversion and serialization.


<h1>2.0 Cloning the Project</h1>

In Github, we clone the repository by using the git clone. The git clone command is used to create a copy of a specific repository or branch within a repository.

Git is a distributed version control system. Maximize the advantages of a full repository on your own machine by cloning.

<h2>Steps to Clone</h2>
The steps to Initiation a git clone.<br>
1. Create a folder in the local machine to clone your remote repository into by using the keyword in windows "mkdir {directory-name}", after initially setting your terminal to the right directory using the "cd {directory-name}." <br>
Any of the terminal on your system can be used for handling git provided it is already installed on your system. Be it Powershell, CommandPrompt, Git Bash, VS Code and even Git GUI.<br>
2. Cloning the git repository into the folder created using the `git clone` https://github.com/oakerekan/altschool-first-semester.git/ command. <br>

When you clone a repository, you don't get one file, like you may in other centralized version control systems. By cloning with Git, you get the entire repository - all files, all branches, and all commits.

<p>Cloning a repository is typically only done once, at the beginning of your interaction with a project. Once a repository already exists on a remote, like on GitHub, then you would clone that repository so you could interact with it locally. Once you have cloned a repository, you won't need to clone it again to do regular development.</p>

<p>The ability to work with the entire repository means that all developers can work more freely. Without being limited by which files you can work on, you can work on a feature branch to make changes safely.</p>


<h1> 3.0 How to Run the Expense Tracker</h1>

The provided code is a script to demonstrate the functionality of an expense tracking system using the **Expense** and **ExpenseDatabase** classes. Breaking it down in bits to help explain the implementation. <br>

<h2> 3.1 Creating Expense Instances:</h2>

```python
expense_1 = Expense(title="fuel", amount=10000)
expense_2 = Expense(title="transport", amount=2000)
expense_3 = Expense(title="data", amount=1000)
expense_4 = Expense(title="food", amount=3000)
expense_5 = Expense(title="shoes", amount=10000)
expense_6 = Expense(title="shoes", amount=300000)
```

<h2>3.2 Creating ExpenseDatabase Instance:</h2>

```python
edb = ExpenseDatabase()
```

<h2>Adding Expenses to the Database:</h2>

```python
for expense in [expense_1, expense_2, expense_3, expense_4, expense_5, expense_6]:
    edb.add_expense(expense)
    print(edb.database)
    print()
    print("-" * 30)
    print()
```
This part of the code adds each expense to the **ExpenseDatabase** and prints the database after each addition.


<h2>3.3 Updating an Expense:</h2>

```python
print(expense_1.update(title="food", amount=5000))
```
This part of the code updates expense_1 with a new title ("food") and amount (5000)

<h2>3.4 Removing an Expense</h2>

```python
print(edb.remove_expense(expense_id=expense_2.id))
```
This part of the code removes the expense with **expense_2's ID** from the ExpenseDatabase.

<h2>3.5 Fetching an Expense by ID or Title:</h2>
```python
print(edb.get_expense_by_id(expense_id=expense_1.id))
print(edb.get_expense_by_title(expense_title="shoes"))
```
These lines fetch an expense by its ID and title from the ExpenseDatabase.

<h2>3.6 Converting ExpenseDatabase to a dict of Dictionaries:</h2> 
```python
print(edb.to_dict())
```
This part of the code prints the ExpenseDatabase converted to a dictionary of dictionaries.

Note: The to_dict method is likely designed to convert the ExpenseDatabase contents into a dict of dictionaries for easy representation or serialization.

Overall, the code provides a basic illustration of expense management functionalities using the defined classes.

