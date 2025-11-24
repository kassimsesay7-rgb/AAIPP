def read_file(test_file):
    """
    Read and return the contents of a file with proper error handling.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        str: The contents of the file
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the user does not have permission to read the file
        IsADirectoryError: If the path points to a directory instead of a file
        IOError: For other I/O related errors
    """
    try:
        with open(test_file, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{test_file}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot read '{test_file}'.")
    except IsADirectoryError:
        raise IsADirectoryError(f"'{test_file}' is a directory, not a file.")
    except IOError as e:
        raise IOError(f"An error occurred while reading '{test_file}': {str(e)}")


# Example usage and testing:
if __name__ == "__main__":
    # Test with a valid file (you may need to create a test file)
    try:
        # Example: Create a test file
        with open("test_file.txt", "w") as f:
            f.write("Hello, World!\nThis is a test file.")
        
        # Read the test file
        content = read_file("test_file.txt")
        print("File content:")
        print(content)
        
        # Test error handling - file not found
        print("\nTesting error handling:")
        try:
            read_file("non_existent_file.txt")
        except FileNotFoundError as e:
            print(f"Caught expected error: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

