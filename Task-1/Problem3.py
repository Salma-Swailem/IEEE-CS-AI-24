import math

x = int(input())

try:
    print(f"The factorial of {x} is {math.factorial(x)}")
except ValueError:
    print(f"Number {x} is not a positive number")
