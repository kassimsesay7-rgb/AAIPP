class Student:
    """Represents a student and their associated marks."""

    def __init__(self, name: str, age: int, mark1: float, mark2: float, mark3: float) -> None:
        """Initialize the student with their name, age, and three marks."""
        self.name = name
        self.age = age
        self.marks = [mark1, mark2, mark3]

    def describe(self) -> None:
        """Print a readable summary of the student's basic information."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self) -> float:
        """Return the total of all recorded marks."""
        return sum(self.marks)
s = Student("john", 21, 85, 90, 88)
s.describe()
print("Total Marks:", s.total_marks())
