#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # This line generates a random number

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
