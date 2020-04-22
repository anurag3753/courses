"""
sorting and grouping in python

Note, change in portfolio will not work correctly

"""
from data_structure_v5 import *

for holding in portfolio:
    print(holding)

## How can I sort on a dict ??
""" 
>>> portfolio.sort()                # This will fail

We need to write our own function, to let python know, how to sort a dictionary
"""

def sort_on_holding_name(holding):
    return[holding['name']]

# Sort portfolio base on stock name
portfolio.sort(key=sort_on_holding_name)
print(portfolio)

# Sort based on shares qty
portfolio.sort(key=lambda holding : holding['shares'])
print(portfolio)

"""
Lets understand lambda function :-
lambda are the anonymous functions, they do not have any names.
They have only two things :- 
    - args they take as input
    - and calculation that they perform on those arguments
    - they default return the value of the expression that gets evaluated

Ex:

>>> a = lambda x : 10 * x             # Meaning is :- a function that excepts one arg and return the arg_value times 10
>>> a(10)
>>> 100

>>> b = lambda x, y : x + y           # Meaning is:- a function that excepts two args and return their sum
>>> b(2, 3)
>>> 5
"""

# How to get the minimum price in the portfolio
minimum_price = min(portfolio, key= lambda holding : holding['price'])
print("minimum price : {}".format(minimum_price))

"""
Grouping the data :- we need to use itertools module
"""
import itertools
# itertools group by two things, 
# 1- key by which you grouped
# 2 - items that come under that group
print(""""""""""------------------""""""""""\n", portfolio)
for name, items in itertools.groupby(portfolio, key=lambda holding : holding['name']):
    print('name :', name)
    for it in items:
        print("     ", it)

# Grouping by name
by_name = { name : list(items)
            for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name'])}
## Give me all the entries for IBM
print(by_name['IBM'])