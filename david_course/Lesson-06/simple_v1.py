"""
In this we are going to learn the basics for `import` statement in python. Do this exercise in python prompt

Theory :-   Feature 1
The way you use your piece of code in some other python code, the way is to import you module, i.e
>>> import simple

    Python goes and finds your code, if found then the python actually execute it as a script from top
    to bottom. The execution takes place in an isolated environment, i.e. anything that is contained in
    that environment, is made available to user like `simple.x`. This way user does not interfere with
    the global namespace variables.

>>> simple

    When you do import then module gets created, and the contents of that module goes inside its own namespace
    
>>> simple.x
>>> simple.spam()
>>> simple.run()

    In order to access any of the variables from the module, you need to call it with the module name, i.e
    You should be able to access the variables and run the functions in thay namespace.

    You can verify that it does not interfere with global namespace, by doing the below experiment:-
>>> x = 17
17
>>> simple.x
42

    You can actually see this with other modules too.
>>> import math
>>> math.cos(2)

"""

x = 42

def spam():
    print("x is :", x)

def run():
    print("Calling spam")
    spam()

print("Running")
run()