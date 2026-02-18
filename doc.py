
def is_even(n):
    """
    Checks whether a number is even.

    >>> is_even(4)
    True
    >>> is_even(5)
    False
    >>> is_even(0)
    True
    """
    return n % 2 == 0


def print_string(s):
    """
    chechs it is a string.

    >>> print_string("I am Sam")
    I am Sam

    >>> print_string("I am an Intern")
    I am an Intern

    :param s: A string to print
    :type s: str
    """
    print(s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()