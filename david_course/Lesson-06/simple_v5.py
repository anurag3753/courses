"""
In this we are going to learn the basics for `import` statement in python. Do this exercise in python prompt
Check for feature 1 in v1, feature 2 in v2, feature 3 in v3, feature 4 in v4

Theory :-   Feature 5

One of the thing, you noticed that if you import the simple_v4, it started printing things. This is called
sideeffect of the source code. You do not want that. So, you move your source code inside a wrapper of __main__

>>> if __name__ == '__main__':
        print("Running")
        run()

>>> import simple_v5        # It does not print thigs now. So, sideeffect is removed

How it works ??
    - Every single module knows, its own name. You can check this by :-

>>> __name__    # It is a global variable and will tell you the global namespace.
'__main__'

If you are the main program or you are the interactive shell, then your name is __main__
On the other hand, if you are imported, then your name is set to your module name

>>> import simple_v5
>>> simple_v5.__name__
'simple_v5'

"""

x = 42

def spam():
    print("x is :", x)

def run():
    print("Calling spam")
    spam()

if __name__ == '__main__':
    print("Running")
    run()