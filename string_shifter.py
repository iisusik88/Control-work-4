def shifting_letters(s: str, shifts: list) -> str:
    """
    Shift each letter in the string by the cumulative sum of shifts from its position to the end.

    Args:
        s: String of lowercase English letters
        shifts: List of integers representing shift amounts

    Returns:
        str: Result string after applying all shifts
    """
    n = len(s)
    chars = list(s)
    total_shift = 0

    # Process from the end to avoid recalculating
    for i in range(n - 1, -1, -1):
        total_shift += shifts[i]
        # Apply shift to current character
        new_char_code = (ord(chars[i]) - ord('a') + total_shift) % 26
        chars[i] = chr(new_char_code + ord('a'))

    return ''.join(chars)


if __name__ == '__main__':
    # Test cases
    test_cases = [
        ("abc", [3, 5, 9]),
        ("aaa", [1, 2, 3]),
        ("z", [1]),
        ("abc", [0, 0, 0]),
        ("xyz", [1, 1, 1])
    ]

    print("Testing shifting_letters function:")
    print("=" * 40)

    for s, shifts in test_cases:
        result = shifting_letters(s, shifts)
        print(f"Input: s = '{s}', shifts = {shifts}")
        print(f"Output: '{result}'")

        # Show explanation for examples
        if s == "abc" and shifts == [3, 5, 9]:
            print("Explanation: 'abc' → 'rpl'")
            print("  shift('a' by 3) = 'd'")
            print("  shift('ab' by 5) = 'ig'")
            print("  shift('abc' by 9) = 'rpl'")
        elif s == "aaa" and shifts == [1, 2, 3]:
            print("Explanation: 'aaa' → 'gfd'")
            print("  shift('a' by 1) = 'b'")
            print("  shift('aa' by 2) = 'dc'")
            print("  shift('aaa' by 3) = 'gfd'")
        print("-" * 30)