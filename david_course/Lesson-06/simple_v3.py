"""
In this we are going to learn the basics for `import` statement in python. Do this exercise in python prompt
Check for feature 1 in v1, feature 2 in v2

Theory :-   Feature 3
>>> import simple_v3       # If you do it, you see the code running
>>> Running
Calling spam
x is : 42
>>> import simple_v3       # Code does not ran, reason is code is already sitting in the main memory. Python imports
                             the module one time, then it sits in cache, and python never reloads the module.

Where the cache is maintained ??
- in sys, there is a function called sys.modules. It is actually a dictionary. If you do 
>>> import sys
>>> sys.modules['simple_v3']  # You can see, your modules already sitting there

If you still want to reload the module, you can delete it from sys.modules and then if you give `import simple_v3`,
it will reload the module
>>> del sys.modules['simple_v3']                 # Not recommended
>>> import simple_v3
>>> Running
Calling spam
x is : 42
"""

x = 42

def spam():
    print("x is :", x)

def run():
    print("Calling spam")
    spam()

print("Running")
run()