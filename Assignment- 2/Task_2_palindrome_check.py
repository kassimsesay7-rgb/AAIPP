'''Task Description #2
   Compare Gemini and Copilot outputs for a palindrome check function.'''


from __future__ import annotations


def is_palindrome(
    text: str,
    *,
    ignore_case: bool = True,
    ignore_non_alnum: bool = True,
) -> bool:
    """
    Return True if `text` is a palindrome.
    By default, ignores case and non-alphanumeric characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    processed = text.casefold() if ignore_case else text
    if ignore_non_alnum:
        processed = "".join(ch for ch in processed if ch.isalnum())

    i, j = 0, len(processed) - 1
    while i < j:
        if processed[i] != processed[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    examples = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "No lemon, no melon",
        "hello",
    ]
    for ex in examples:
        print(f"{ex!r}: {is_palindrome(ex)}")


