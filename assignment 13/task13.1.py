import math

def calculate_area(shape, x, y=None):
    shape = shape.lower()
    if shape == "rectangle":
        if y is None:
            raise ValueError("Rectangle requires both length and width.")
        return x * y
    if shape == "square":
        return x * x
    if shape == "circle":
        return math.pi * x * x
    raise ValueError(f"Unsupported shape: {shape}")
# Example usage:
print(calculate_area("rectangle", 5, 10))  # Output: 50
print(calculate_area("square", 4))          # Output: 16
print(calculate_area("circle", 3))          # Output: 28.274333882308138