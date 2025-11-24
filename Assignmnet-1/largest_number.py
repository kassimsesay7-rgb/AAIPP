def find_largest_number(numbers):
    """
    Returns the largest number in a list.
    Args:
        numbers (list): List of numeric values.
    Returns:
        The largest number in the list, or None if the list is empty.
    """
    if not numbers:
        return None
    return max(numbers)

# Example usage:
if __name__ == "__main__":
    sample_list = [3, 5, 2, 8, 1]
    largest = find_largest_number(sample_list)
    print(f"The largest number in {sample_list} is {largest}")
# Review:
# - Uses Python's built-in max() function, which is efficient (O(n) time).
# - Handles empty lists gracefully by returning None.
# - Code is concise, readable, and leverages standard library features.
# - For very large lists, this is as efficient as possible in Python.