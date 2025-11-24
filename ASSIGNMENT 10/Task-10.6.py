def grade(score: int) -> str:
    """
    Determine the letter grade for a given numeric score.

    Parameters:
        score (int): The score to evaluate. Must be in the range 0-100.

    Returns:
        str: The letter grade ('A', 'B', 'C', 'D', or 'F').

    Raises:
        ValueError: If the score is not within 0 to 100 (inclusive).
    """
    if not isinstance(score, int) or not (0 <= score <= 100):
        raise ValueError("Score must be an integer between 0 and 100 (inclusive).")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Boundary test cases
for test_score in [90, 80, 70, 60, 100, 0]:
    print(f"grade({test_score}) = {grade(test_score)}")
