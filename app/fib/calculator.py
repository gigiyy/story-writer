"""Fibonacci calculator module."""
from typing import Union

def calculate_fibonacci(n: Union[int, float]) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n (Union[int, float]): The index of the Fibonacci number to calculate.
            Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    # Input validation
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a non-negative integer")
    if not float(n).is_integer():
        raise ValueError("Input must be a non-negative integer")
    n = int(n)
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Base cases
    if n <= 1:
        return n

    # Calculate Fibonacci number iteratively for better performance
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b