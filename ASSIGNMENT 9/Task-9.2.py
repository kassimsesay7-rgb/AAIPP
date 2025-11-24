class SruStudent:
    """Class representing an SR University student."""

    def __init__(self, name, roll_no, hostel_status):
        # Initialize student name, roll number, and hostel status
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = 0  # total fee paid so far

    def fee_update(self, amount):
        """Update the fee paid by the student."""
        # ensure valid amount
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.fee_paid += amount

    def display_details(self):
        """Return formatted student details."""
        return (
            f"Name: {self.name}, Roll: {self.roll_no}, "
            f"Hostel: {self.hostel_status}, Fee Paid: {self.fee_paid}"
        )


if __name__ == "__main__":
    s = SruStudent("Anu", "CS2025", "Yes")
    s.fee_update(5000)
    print(s.display_details())
    # expected: Name: Anu, Roll: CS2025, Hostel: Yes, Fee Paid: 5000
