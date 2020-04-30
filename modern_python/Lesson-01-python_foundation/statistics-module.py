""" We are going to see the statistics module present in python.

Technical :- Statistics module was designed for accuracy. It returns accuracy
            till 17 decimal places. However it is argued that, for simple things
            like average, is it good to return the anwer till 17 places.
"""
from statistics import mode, median, mean, stdev, pstdev

def use_statistics():
    ''' Median is mainly used for unbalanced distributions
    pstdev : It is same as, when you divide by number `n`
    stddev : divide factor is `n-1`. Rest is same

    >>> mean([50, 52, 53])
    51.666666666666664
    >>> mode([50, 50, 50, 51, 41, 42, 42])
    50
    >>> median([51, 50, 50, 53])
    50.5
    >>> stdev([51, 50, 52, 53, 51, 51])
    1.0327955589886444
    >>> pstdev([51, 50, 52, 53, 51, 51])
    0.9428090415820634

    '''


if __name__ == '__main__':
    import doctest
    doctest.testmod()