# Write a Python Function to find factorial of given number with recursion.

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(10))
