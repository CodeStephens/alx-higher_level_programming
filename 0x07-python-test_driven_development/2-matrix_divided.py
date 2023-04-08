#!/usr/bin/python3 


def add_integer(a, b=98):
    """ adds two given values (either integer or float) together """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer or b must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("a must be an integer or b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
