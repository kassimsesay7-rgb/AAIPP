def is_valid_email(email: str) -> bool:
	"""
	Simple email validator based on the given requirements:
	- Must contain '@' and '.' characters
	- Must not start or end with special characters
	- Should not allow multiple '@'
	For "special characters", we consider any non-alphanumeric character as special.
	"""
	if not isinstance(email, str) or not email:
		return False
	# Must contain '@' and '.' characters
	if '@' not in email or '.' not in email:
		return False
	# Should not allow multiple '@'
	if email.count('@') != 1:
		return False
	# Must not start or end with special characters (only allow alphanumeric at boundaries)
	if not email[0].isalnum() or not email[-1].isalnum():
		return False
	return True


def run_tests() -> None:
	# AI-generated test cases covering the stated requirements
	valid_emails = [
		"user@example.com",
		"a.b-c_d1@sub.domain.co",
		"user_name@domain.com",
		"x@x.x",
		"JohnDoe123@company.org",
	]
	invalid_emails = [
		".user@example.com",     # starts with special
		"user@example.com.",     # ends with special
		"user@@example.com",     # multiple @
		"userexample.com",       # missing @
		"user@example",          # missing .
		"@example.com",          # starts with @ (special)
		"user@domain.com.",      # ends with .
		"",                      # empty string
		12345,                   # non-string input
	]

	total = 0
	passed = 0

	for e in valid_emails:
		total += 1
		try:
			if is_valid_email(e):
				passed += 1
			else:
				print(f"FAIL (expected valid): {e}")
		except Exception as ex:
			print(f"EXCEPTION (expected valid): {e} -> {ex}")

	for e in invalid_emails:
		total += 1
		try:
			if not is_valid_email(e):  # should be invalid
				passed += 1
			else:
				print(f"FAIL (expected invalid): {e}")
		except Exception:
			# Treat exceptions as failure of validation function contract
			# (Function should return bool, not raise)
			print(f"EXCEPTION (expected invalid but raised): {e}")

	print(f"Passed {passed}/{total} tests")


if __name__ == "__main__":
	run_tests()


