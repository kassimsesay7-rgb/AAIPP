'''Task Description#4
    • Install and configure Cursor AI. Use it to generate a 
    Python function (e.g., sum of squares).'''


def sum_of_squares(numbers_list):
    """
    Calculates the sum of the squares of all numbers in a given list.
    
    Args:
        numbers_list (list): A list containing numerical values.
        
    Returns:
        float or int: The total sum of the squares of the list elements.
    """
    total_sum_of_squares = 0
    
    # Iterate through each number in the list
    for num in numbers_list:
        # Square the current number (num * num or num**2)
        squared_num = num ** 2
        
        # Add the squared result to the running total
        total_sum_of_squares += squared_num
        
    return total_sum_of_squares

# --- Example Usage ---
data = [1, 2, 3, 4]
result = sum_of_squares(data)

print(f"The list of numbers is: {data}")
print(f"Calculation: (1² + 2² + 3² + 4²) = (1 + 4 + 9 + 16) = {result}") 
# Expected Output: 30