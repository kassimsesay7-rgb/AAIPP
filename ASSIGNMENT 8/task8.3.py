import re

def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a given sentence is a palindrome.
    Ignores case, spaces, and punctuation.
    Digits are considered part of the content.
    """
    # Remove all non-alphanumeric characters using regex
    cleaned = re.sub(r'[^A-Za-z0-9]', '', sentence).lower()

    # Compare cleaned string with its reverse
    return cleaned == cleaned[::-1]



def run_tests() -> None:
	"""
	AI-generated test cases for is_sentence_palindrome(sentence).
	Assumptions:
	- Palindrome check ignores case, spaces, and punctuation.
	- Digits are considered part of the content (i.e., kept for palindrome checks).
	- An empty string (or a string with only spaces/punctuation) is a palindrome.
	"""
	try:
		_ = is_sentence_palindrome  # type: ignore[name-defined]
	except NameError:
		print("is_sentence_palindrome(sentence) is not defined. Please implement it before running tests.")
		return

	test_cases = [
		# True cases (classic sentences / common examples)
		("A man a plan a canal Panama", True),
		("No lemon, no melon", True),
		("Was it a car or a cat I saw?", True),
		("Able was I, ere I saw Elba!", True),
		("Madam, I'm Adam.", True),
		("Never odd or even", True),
		("Step on no pets", True),
		("Don't nod", True),
		("Eva, can I see bees in a cave?", True),
		# digits and alphanumerics
		("12321", True),
		("1 2 3 2 1", True),
		("123abccba321", True),
		# mixed punctuation/spacing/case
		(".,,   ", True),                  # reduces to empty -> palindrome
		("", True),                        # empty string
		("   ", True),                     # spaces only
		("Rats live on no evil star!", True),
		("Yo, Banana Boy!", True),

		# False cases
		("Hello, World!", False),
		("This is not a palindrome", False),
		("Palindrome", False),
		("No lemon, some melon", False),
		("Was it a car or a dog I saw?", False),
		("123456", False),
		("Madam I'm not Adam", False),
	]

	total = 0
	passed = 0

	for sentence, expected in test_cases:
		total += 1
		try:
			result = is_sentence_palindrome(sentence)  # type: ignore[name-defined]
			if result == expected:
				passed += 1
			else:
				print(f"FAIL: input={sentence!r}, expected={expected}, got={result}")
		except Exception as ex:
			print(f"EXCEPTION: input={sentence!r}, expected={expected}, ex={ex}")

	print(f"Passed {passed}/{total} tests")


if __name__ == "__main__":
	run_tests()

