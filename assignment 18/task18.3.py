def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
print(f"Input: 5 → Output: Factorial = {factorial(5)}")
print(f"Input: 0 → Output: Factorial = {factorial(0)}")
