
"""
Calculator module providing basic arithmetic operations.

Functions
---------
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Difference (a - b).
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divide a by b.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        Quotient of a / b.

    Raises
    ------
    ZeroDivisionError
        If b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == "__main__":
    print("add:", add(4,2))        # expected 6
    print("sub:", subtract(4,2))   # expected 2
    print("mul:", multiply(4,2))   # expected 8
    print("div:", divide(4,2))     # expected 2.0
    try:
        divide(4,0)
    except Exception as e:
        print("divide(4,0) raised:", type(e).__name__)  # expected ZeroDivisionError
