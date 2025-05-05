#!/usr/bin/python3
import sys

def factorial(n):

	"""
	Function to calculate the factorial of a given number `n` using recursion.

	Parameters:
	-----------
	n : int
		The number for which the factorial is to be calculated. It must be a non-negative integer.

	Returns:
	--------
	int
		The factorial of the input number `n`. The factorial of 0 is defined as 1.

	Example:
	--------
	factorial(5) -> 120
	factorial(0) -> 1
	"""

	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
