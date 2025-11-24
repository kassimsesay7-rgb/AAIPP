def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    num = input("Enter a number (or type 'quit' to exit): ")

    # Check if user wants to quit
    if num.lower() == "quit":
        break

    # Check if input is a valid number before converting
    if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
        num = int(num)
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    else:
        break # Exit on invalid input

