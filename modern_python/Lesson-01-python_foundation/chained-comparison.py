""" Chained Comparison
"""

def chained_comparison_usage():
    '''
    >>> x = 20
    >>> x > 10 and x < 20
    False
    >>> 10 < x < 20             # Chained Comparison
    False
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()