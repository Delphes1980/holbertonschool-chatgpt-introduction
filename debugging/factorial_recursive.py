#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n recursively.

    Parameters:
    n (int): A non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the number from command-line argument, compute and print the factorial
f = factorial(int(sys.argv[1]))
print(f)
