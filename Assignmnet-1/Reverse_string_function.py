# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# test the function
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: \n")
    reversed_str = reverse_string(user_input)
    print(f'The original string is: {user_input}')
    print(f"The reversed string is: {reversed_str}")