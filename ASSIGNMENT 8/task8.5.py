def convert_date_format(date_str: str) -> str:
    """
    Convert date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format.

    Example:
        Input:  "2023-10-15"
        Output: "15-10-2023"
    """
    try:
        year, month, day = date_str.split("-")
        return f"{day}-{month}-{year}"
    except ValueError:
        raise ValueError("Invalid date format. Expected 'YYYY-MM-DD'.")






def run_tests() -> None:
	"""
	AI-generated tests for convert_date_format(date_str).
	Contract assumptions:
	- Input strings follow the ISO format "YYYY-MM-DD".
	- Output should be returned as "DD-MM-YYYY".
	- The function returns a string and should not mutate the input.
	"""
	try:
		_ = convert_date_format  # type: ignore[name-defined]
	except NameError:
		print("convert_date_format(date_str) is not defined. Please implement it before running tests.")
		return

	tests = []

	def test_basic_conversion() -> None:
		assert convert_date_format("2023-10-15") == "15-10-2023", "Example date should swap year/month/day order"

	tests.append(("basic conversion", test_basic_conversion))

	def test_single_digit_month_and_day() -> None:
		assert convert_date_format("2023-01-09") == "09-01-2023", "Leading zeros must be preserved during conversion"

	tests.append(("single-digit month/day", test_single_digit_month_and_day))

	def test_end_of_year() -> None:
		assert convert_date_format("1999-12-31") == "31-12-1999", "Date at end of year should convert correctly"

	tests.append(("end of year conversion", test_end_of_year))

	def test_leap_day() -> None:
		assert convert_date_format("2020-02-29") == "29-02-2020", "Leap day should remain valid after conversion"

	tests.append(("leap day conversion", test_leap_day))

	def test_minimum_padded_values() -> None:
		assert convert_date_format("0001-01-01") == "01-01-0001", "Zero-padded boundaries should be preserved"

	tests.append(("minimum padded values", test_minimum_padded_values))

	total = len(tests)
	passed = 0

	for description, test in tests:
		try:
			test()
			passed += 1
		except AssertionError as ex:
			print(f"FAIL: {description} -> {ex}")
		except Exception as ex:
			print(f"EXCEPTION: {description} -> {type(ex).__name__}: {ex}")

	print(f"Passed {passed}/{total} tests")


if __name__ == "__main__":
	run_tests()

