"""Calculate the nth Fibonacci number using recursion and document the logic."""


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using a recursive definition."""
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


EXPLANATION = """
Function name: fibonacci

Purpose:
    Calculate the Fibonacci value at a zero-based index.

Inputs:
    n (int) – the sequence index. Must be non-negative.

Process:
    * Guard clause raises ValueError when n is negative.
    * Base cases handle n == 0 and n == 1.
    * For n >= 2, the function recurses: F(n) = F(n-1) + F(n-2).

Outputs:
    Returns the integer Fibonacci value at index n.

Notes on complexity:
    * Time complexity is exponential (O(φ^n)) due to repeated subproblems.
    * Space complexity equals recursion depth, O(n).
"""


def explain() -> str:
    """Provide the human-readable explanation of how fibonacci works."""
    return EXPLANATION



# Get the output of the fibonacci function
print(fibonacci(10))

# Get the output of the explain function
print(explain())