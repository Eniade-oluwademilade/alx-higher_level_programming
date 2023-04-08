#!/usr/bin/python3

"""Function adds two integers"""

def add_integer(a, b=98):
    """Adds two integers
        a: an int or float
        b: an int or float
    Returns an addition of a and b
    """

    if ((not isinstance(a, int) or (a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) or (b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
