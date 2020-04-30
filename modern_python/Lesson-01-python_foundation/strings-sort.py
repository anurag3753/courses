"""It contains the details about below functions
    - list usages
    - sort vs sorted
    - string (index and count methods)
"""

def use_string():
    '''
    All the iterables have a method `count` and you can check the supported methods
    by running dir(list) :- It will list all the methods for `list`

    sort vs sorted :-
        sort :- Inplace sort the list
        sorted :- Gives a sorted list copy (it runs on immutable objects too)
            - It is more convenient to use, because you do not need to convert elements
            to list first, whereas in `sort()` you need to do that.

    >>> s = [ 20, 30, 10 ]
    >>> t = [40, 50, 60 ]
    >>> u = s + t
    >>> u[-2:]
    [50, 60]
    >>> s = 'abbarakadaabra'
    >>> i = s.index('k')
    >>> i
    6
    >>> s.count('a')
    7
    >>> s = [ 20, 30, 10]
    >>> s.sort()
    >>> s
    [10, 20, 30]
    >>> s = [ 20, 10, 30, 40 ]
    >>> t = sorted(s)
    >>> t
    [10, 20, 30, 40]
    >>> s
    [20, 10, 30, 40]


    >>> s = 'cat'
    >>> s.sort()                                    # It failed as expected, sort does not work on immutable objs
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'str' object has no attribute 'sort'
    >>> sorted(s)
    ['a', 'c', 't']

    '''