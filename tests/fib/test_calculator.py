"""Tests for the Fibonacci calculator functionality."""
import pytest
from app.fib.calculator import calculate_fibonacci

def test_fibonacci_zero():
    """Test Fibonacci calculation for n=0."""
    assert calculate_fibonacci(0) == 0

def test_fibonacci_one():
    """Test Fibonacci calculation for n=1."""
    assert calculate_fibonacci(1) == 1

def test_fibonacci_positive():
    """Test Fibonacci calculation for positive numbers."""
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(6) == 8
    assert calculate_fibonacci(7) == 13

def test_fibonacci_negative():
    """Test that negative numbers raise ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_fibonacci(-1)

def test_fibonacci_non_integer():
    """Test that non-integer inputs raise ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_fibonacci(3.5)