def check_number(num):
    if num > 0:
        print(f"Input: {num} → Output: The number is positive")
    elif num < 0:
        print(f"Input: {num} → Output: The number is negative")
    else:
        print(f"Input: {num} → Output: The number is zero")

# Calling the function
check_number(-5)
check_number(0)
check_number(7)
