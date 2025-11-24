# Recursive version of factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative version of factorial
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
if __name__ == "__main__":
    num = 5
    print("Recursive:", factorial_recursive(num))  # Output: 120
    print("Iterative:", factorial_iterative(num))  # Output: 120