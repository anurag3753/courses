"""We are going to learn about Counter object. It is a part of collections
module. But we have very rarely used it. It is very good and in some sense
similar to a dict with more and more features.

This is very popular in data analytics world. It is suitable for counting
and hence the name Counter suits it.

In doctest if we do not get anything. That means it is a perfect pass

"""

from collections import Counter

""" Problem 1 :- If a key is not present. Python default will error out.
Ex: How many dragons you have ??

d = {}
print (d['dragons']) # It will error out as python with Keyerror

    Solution :- But in many data analytics scanerio. If sth does not exists you want to report default as 0.
                So, here you can use counter to achieve it.
"""
d = Counter()
print(f"Total dragons: {d['dragons']}")         # It does not error out, if sth does not exists it will return default as 0
d['dragons'] += 1           # Increment dragons by 1. It works like regular dict

def counter_use():
    """ Problem 2 :- Count the number of objects. Rather than using loop in general scanerio,
                 Counter does it automatically and it uses these thigs internally

    >>> Counter('red green blue red red green blue blue blue blue'.split())
    Counter({'blue': 5, 'red': 3, 'green': 2})

    >>> c = Counter('red green blue red red green blue blue blue blue'.split())
    >>> c.most_common()
    [('blue', 5), ('red', 3), ('green', 2)]

    >>> c.most_common(2)                        # It returns two most common items
    [('blue', 5), ('red', 3)]

    >>> list(c.elements())                      # Get all the elements from Counter object. Since it is a dict, order is not guaranteed
    ['red', 'red', 'red', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue']

    >>> list(c)                                 # Get keys for dict
    ['red', 'green', 'blue']

    >>> list(c.values())                        # Get values
    [3, 2, 5]

    >>> list(c.items())                         # Get all items
    [('red', 3), ('green', 2), ('blue', 5)]
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()