"""Test module for Fibonacci calculator."""
import pytest

from app.fib.calculator import FibCalculator


def test_fibonacci_zero():
    """Test fibonacci of 0."""
    calculator = FibCalculator()
    assert calculator.calculate(0) == 0


def test_fibonacci_one():
    """Test fibonacci of 1."""
    calculator = FibCalculator()
    assert calculator.calculate(1) == 1


def test_fibonacci_small_number():
    """Test fibonacci of small number."""
    calculator = FibCalculator()
    assert calculator.calculate(7) == 13


def test_fibonacci_large_number():
    """Test fibonacci of large number with caching."""
    calculator = FibCalculator()
    assert calculator.calculate(40) == 102334155
    # second call should use cache
    assert calculator.calculate(40) == 102334155


def test_fibonacci_negative_number():
    """Test fibonacci of negative number raises ValueError."""
    calculator = FibCalculator()
    with pytest.raises(ValueError, match="Input must be non-negative"):
        calculator.calculate(-1)


def test_fibonacci_non_integer():
    """Test fibonacci of non-integer raises ValueError."""
    calculator = FibCalculator()
    with pytest.raises(ValueError, match="Input must be an integer"):
        calculator.calculate(1.5)


def test_fibonacci_too_large():
    """Test fibonacci of too large number raises ValueError."""
    calculator = FibCalculator()
    with pytest.raises(ValueError, match="Input must be less than or equal to 100"):
        calculator.calculate(101)

