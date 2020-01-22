Manage Your Expenses

A django Application to manage your expenses.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.5 or higher installed on your system
2. pip installed on your system
3. git installed on your system
4. postgres SQL 9.5.19

You can install this application on an Ubuntu or Windows application, but here we are focussing on installation on Ubuntu. 


### Installing

A step by step series of examples that tell you how to get a development env running


```
1. pip3 install virtualenv   #Install the virtual Environment
2. virtualenv venv           #Create the virtual Environment 
3. source venv/bin/activate  #activate the virtual environment
4. mkdir expense_management
5. cd expense_management
6. git clone https://github.com/desising/espenses.git
7. cd espenses
8. pip install -r requirements.txt 
9. python manage.py migrate
10.python manage.py create superuser
11.python manage.py runserver
12.open your browser and access http://localhost:8000/login
```


