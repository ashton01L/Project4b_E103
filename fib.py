# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/17/2024
# Description: Define a function named fib that takes a positive integer parameter
# and returns the number at that position of the Fibonacci sequence.

def fib(sequential):
    """
    A function that takes a positive integer parameter and then returns the number at
    that position of the Fibonacci sequence
    :param sequential: sequential integer which corresponds to the specific position in the Fibonacci sequence.
    :return: fib (int) = corresponding number of specific Fibonacci sequential
    """
    if sequential < 0:
        return "Invalid Input"
    elif sequential == 0:
        return 0
    elif sequential == 1:
        return 1

    a, b = 1, 1
    for _ in range(sequential - 2):
        a, b = b, a + b
    return b

# sequential = 10
# print(fib(sequential))
