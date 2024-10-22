#pair: Aisha & Afrah
import unittest

from fibonacci import fibonacci_recursive

def test_fibonacci_recursive():
    #numbers i expect for the first 10 indices
    expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i in range(len(expected_values)):
        result = fibonacci_recursive(i)
        assert result == expected_values[i], f"Test failed for n={i}: expected {expected_values[i]}, got {result}"
        print(f"Fibonacci({i}) = {result} (Test passed)")

# Runing our tests
if __name__== "_main_":
    test_fibonacci_recursive()