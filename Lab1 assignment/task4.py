import math
from typing import Any


def factorial_recursive(n: int) -> int:
    """Compute n! using recursion.

    Comments:
    - Base case: 0! = 1 and 1! = 1
    - Recursive step: n! = n * (n-1)!
    - Time complexity: O(n)
    - Space complexity: O(n) due to recursion call stack

    Args:
        n: Non-negative integer

    Returns:
        n factorial as int

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive: n must be an integer")
    if n < 0:
        raise ValueError("factorial_recursive: n must be non-negative")

    # Base case: 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n * (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Compute n! using an iterative loop.

    Comments:
    - Uses an explicit loop to multiply values from 2..n
    - Time complexity: O(n)
    - Space complexity: O(1) (constant extra space)

    Args:
        n: Non-negative integer

    Returns:
        n factorial as int

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative: n must be an integer")
    if n < 0:
        raise ValueError("factorial_iterative: n must be non-negative")

    result = 1
    # Multiply numbers from 2 up to n (1 does not change the product)
    for i in range(2, n + 1):
        result *= i
    return result


if _name_ == "_main_":
    # Quick checks / demo
    test_values = [0, 1, 5, 10]
    print("Testing factorial implementations...")
    for tv in test_values:
        r_rec = factorial_recursive(tv)
        r_itr = factorial_iterative(tv)
        r_math = math.factorial(tv)
        print(f"{tv}! -> recursive: {r_rec}, iterative: {r_itr}, math.factorial: {r_math}")
        # Ensure both implementations agree with each other and math.factorial
        assert r_rec == r_itr == r_math

    # Test error handling for negatives
    try:
        factorial_recursive(-1)
    except ValueError:
        print("Recursive correctly raised ValueError for -1")

    try:
        factorial_iterative(-2)
    except ValueError:
        print("Iterative correctly raised ValueError for -2")

    # Test type checking
    try:
        factorial_iterative(3.5)  # should raise TypeError
    except TypeError:
        print("Iterative correctly raised TypeError for non-int input")

    print("All checks passed.")
