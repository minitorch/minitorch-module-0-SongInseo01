"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: int, y: int) -> int:
    """
    A function that performs a multiplication function

    Input: x, y (int value)
    Output: k (int value), The result of x multiplying y
    """

    k: int = x * y
    return k


def id(x: int) -> int:
    """
    Returns the input unchanged

    Input: x (int value)
    Output: k (int value), The result of input unchanged
    """

    k: int = x
    return k


def add(x: int, y: int) -> int:
    """
    A function that performs a add function

    Input: x, y (int value)
    Output: k (int value), The result of x add y
    """

    k: int = x + y
    return k


def neg(x: int) -> int:
    """
    Negates a number

    Input: x (int value)
    Output: k (int value), The result of negating x
    """

    k: int = -x
    return k


def lt(x: int, y: int) -> bool:
    """
    Checks if one number is less than another

    Input: x, y (int value)
    Output: result (bool value), True if x is less than y, else False
    """

    result: bool = x < y
    return result


def eq(x: int, y: int) -> bool:
    """
    Checks if two numbers are equal

    Input: x, y (int value)
    Output: result (bool value), True if x is equal to y, else False
    """

    result: bool = x == y
    return result


def max(x: int, y: int) -> int:
    """
    Returns the larger of two numbers

    Input: x, y (int value)
    Output: k (int value), The larger of x and y
    """

    k: int = x if x > y else y
    return k


def is_close(x: int, y: int, tolerance: int = 1) -> bool:
    """
    Checks if two numbers are close in value

    Input: x, y (int value), tolerance (optional int value, default = 1)
    Output: result (bool value), True if the absolute difference between x and y is less than or equal to tolerance
    """

    result: bool = abs(x - y) <= tolerance
    return result

# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
def sigmoid(x: float) -> float:
    """
    Computes the sigmoid function for a given input x.

    Input: x (float value)
    Output: result (float value), The result of the sigmoid function
    """
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))




# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
