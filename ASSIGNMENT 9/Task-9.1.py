def sum_even_odd(numbers):
    """Return sums of even and odd numbers in the given list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        tuple[int, int]: (even_sum, odd_sum)
            even_sum -> total of all even integers
            odd_sum  -> total of all odd integers
    """
    even_sum, odd_sum = 0, 0
    for n in numbers:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum, odd_sum
# -------- AI-generated docstring version (for comparison) --------
def sum_even_odd_ai(numbers):
    """Compute the sum of even and odd integers in a list.

    Parameters
    ----------
    numbers : list
        List containing integers.

    Returns
    -------
    tuple
        (sum_even, sum_odd): sum of even and odd integers respectively.
    """
    even_sum, odd_sum = 0, 0
    for n in numbers:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum, odd_sum


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, -2]
    print("Manual:", sum_even_odd(data))  # expected (12, 9)
    print("AI:", sum_even_odd_ai(data))   # expected (12, 9)
