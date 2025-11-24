def assign_grade(score: int) -> str:
	"""
	Returns a letter grade for a numeric score based on the scheme:
	90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
	Raises ValueError for invalid inputs (non-int or out of [0, 100]).
	"""
	if not isinstance(score, int):
		raise ValueError("score must be an integer")
	if score < 0 or score > 100:
		raise ValueError("score must be between 0 and 100")
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"


def run_tests() -> None:
	# Valid and boundary cases
	valid_cases = [
		(100, "A"),
		(99, "A"),
		(90, "A"),
		(89, "B"),
		(80, "B"),
		(79, "C"),
		(70, "C"),
		(69, "D"),
		(60, "D"),
		(59, "F"),
		(0, "F"),
		# mid-range samples
		(75, "C"),
		(85, "B"),
		(65, "D"),
		(30, "F"),
	]

	# Invalid inputs
	invalid_inputs = [
		-5,         # below range
		105,        # above range
		"eighty",   # wrong type
		None,       # missing value
		89.5,       # non-integer
	]

	total = 0
	passed = 0

	# Test valid cases
	for score, expected in valid_cases:
		total += 1
		try:
			result = assign_grade(score)
			if result == expected:
				passed += 1
			else:
				print(f"FAIL valid: score={score}, expected={expected}, got={result}")
		except Exception as ex:
			print(f"EXCEPTION valid: score={score}, expected={expected}, ex={ex}")

	# Test invalid inputs (should raise ValueError)
	for bad in invalid_inputs:
		total += 1
		try:
			assign_grade(bad)
			print(f"FAIL invalid: input={bad}, expected ValueError, got no exception")
		except ValueError:
			passed += 1
		except Exception as ex:
			print(f"WRONG EXCEPTION invalid: input={bad}, expected ValueError, got {type(ex).__name__}: {ex}")

	print(f"Passed {passed}/{total} tests")


if __name__ == "__main__":
	run_tests()

