# Michelle Patlan
# 8/20/2022
# Problem 2: Write a Python function to check whether a number is in a given range. Use
# range(1,10). Print whether the number is in or not in the range.

#function defined, rang given, if this, else that, give range a number to test
def given_range(n):
    if n in range(1, 10):
        print(" The number is in the range")
    else:
        print("The number is outside the given range.")


given_range(6)
