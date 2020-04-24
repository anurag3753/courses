"""
In this we are going to learn the basics for `import` statement in python. Do this exercise in python prompt
Check for feature 1 in v1, feature 2 in v2, feature 3 in v3

Theory :-   Feature 4

what if the import statement itself fails ??
    - it fails, when python is not able to import the module.

What decide in which path, python will check for the module presence ??
>>> import sys
>>> sys.path       # It is a list of strings. these strings are the paths python consults in order to load your modules.
                   # if your module is, not in the path mentioned by sys.path. Then it will not be loaded.

In order to force python to check in the path where you have defined your module is you can do :-

>>> cd v4
>>> import simple_v4              # It fails, as module is present at one level up

Way1 :-
>>> sys.path.append('..')         # This will force python to check for the code in one level up.
>>> import simple_v4              # PASSED

Way2 :-                           # Only vaild in linux. Not sure about windows
>>> env PYTHONPATH=.. python3     # This will also force python to check the code in one level up
>>> import simple_v4

"""

x = 42

def spam():
    print("x is :", x)

def run():
    print("Calling spam")
    spam()

print("Running")
run()