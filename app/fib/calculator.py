"""Module for Fibonacci number calculation."""


class FibCalculator:
    """A class to calculate Fibonacci numbers efficiently with caching."""

    def __init__(self):
        """Initialize the calculator with an empty cache."""
        self._cache = {0: 0, 1: 1}

    def calculate(self, n: int) -> int:
        """
        Calculate the nth Fibonacci number.

        Args:
            n: The position in the Fibonacci sequence to calculate (0-based)

        Returns:
            The nth Fibonacci number

        Raises:
            ValueError: If n is negative, non-integer, or greater than 100
        """
        # Input validation
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be non-negative")
        if n > 100:
            raise ValueError("Input must be less than or equal to 100")

        # Return cached value if available
        if n in self._cache:
            return self._cache[n]

        # Calculate using dynamic programming approach
        for i in range(2, n + 1):
            if i not in self._cache:
                self._cache[i] = self._cache[i - 1] + self._cache[i - 2]

        return self._cache[n]
