"""
In this we are going to learn the basics for `import` statement in python. Do this exercise in python prompt
Check for feature 1 in v1

Theory :-   Feature 2

>>> from simple_v1 import run

Surprisingly, It also executes the entire file, in a way similar to import. Now type this

>>> x           ## It errors out. So, we only got run and no other functionality
>>> spam()      ## It errors out. So, we only got run and no other functionality
>>> run()       ## It works, but if run calls spam, then how does spam worked if it is not available.

So, what actually happens when you do `from simple_v1 import run`
    - It executes the code from top to bottom, similar to import
    - It then copy the entire namespace available in memory, that is why you managed to access spam
    - Then since, you want only run it does sth like below to make it available to you

>>> run = simple.run    # Copy the run module

Since entire simple is already loaded in main memory. then it just makes a copy of the run function, which the user
has requested. So, people who says, that
    - from simple import run  # is more efficient, as it is only loading a part of file. It is actually not, 
    you already copied the entire namespace in your main memory

Another my confusion:-
>>> from simple import x

Then if we use this in a file, which already has a variable x in its top, then which `x` will be referred ??
    - this newly imported x will overwrite x present in the existing file
>>> x
>>> 42   # since x is overwritten now

What if we do  :-
>>> from simple import spam
>>> x is : 42

Which x it will be referring to ??
    -> One key concept is, every global varaiable is pinned to the file in which it is defined. So, if you do `from simple import spam`
    it will be using the x that is defined in its own module. It will not use the latest x defined in the file.

"""

x = 42

def spam():
    print("x is :", x)

def run():
    print("Calling spam")
    spam()

print("Running")
run()