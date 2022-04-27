# Factorial Function

import math


def factorial(n):

    if n == 0:
        r = 1
    else:
        r = n * math.factorial(n-1)

    print(f'The value of the factorial function for {n} is {r}.')


factorial(int(input("Enter any positive integer or zero:\n")))
