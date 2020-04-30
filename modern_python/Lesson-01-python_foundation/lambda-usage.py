""" What does lambda do ?
        - Makes a function
        - Common use, is to make throw away functions
        - Defer a computation to future / Make a promise in future
            - We only want to run sth in future, when somebody triggers an event
            like in async io type program, or when they trigger an event pressing a
            button, in gui wizard
            - You will always see this in GUI. Some people call it `promises`, some
            call it `thunks`
"""

def lambda_use():
    '''
    >>> lambda x : x * 2
    <function <lambda> at 0x00000236AFD539D8>
    >>> (lambda x : x * 2)(5)
    10
    >>> 100 + (lambda x : x * 2)(5) + 50
    160
    >>> f = lambda x, y : 3*x + y               # this usage of lambda is done in event programming
    >>> f(3, 8)
    17
    '''
