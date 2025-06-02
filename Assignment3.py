'''Assignment 3 Task 1'''

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial(number)}")

'''Assignment 3 Task 2 '''

import math
number = float(input("Enter a number: "))
print(f"Square root: {math.sqrt(number)}")
print(f"Logarithm: {math.log(number)}")
print(f"Sine: {math.sin(number)}")
