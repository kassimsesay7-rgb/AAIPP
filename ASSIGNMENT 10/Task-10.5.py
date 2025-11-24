def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input types, must be numbers."

print(div(10, 0))
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Valid division result: {result}")
        return result
    except ZeroDivisionError:
        print("Division by zero case: Error - Division by zero is not allowed.")
        return None
    except TypeError:
        print("Invalid type input case: Error - Inputs must be numbers.")
        return None

# Example usage:
divide_numbers(20, 4)     # Valid division
divide_numbers(5, 0)      # Division by zero
divide_numbers("a", 2)    # Invalid type input

