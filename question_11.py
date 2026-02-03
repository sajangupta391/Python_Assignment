#Question 11

import sys

def factorial_num(n):
    if not isinstance(n, int):
        raise TypeError(f"Factorial only defined integers: {type(n).__name__}")

    if n < 0:
        raise ValueError("Factorial not defined negative numbers.")

    if n == 0 or n == 1:
        return 1
    
    try:
        return n * factorial_num(n - 1)
    except RecursionError:
        raise RecursionError("Input too large for recursive calculation. Try an approach.")

test_inputs = [5, -1, 4.5, "hello", 0]

print("Starting \n")

for val in test_inputs:
    try:
        result = factorial_num(val)
        print(f"Input: {val} Result: {result}")
    
    except (ValueError, TypeError, RecursionError) as e:
        print(f"Input: {val} Error: {e}")

print("\n Complete")