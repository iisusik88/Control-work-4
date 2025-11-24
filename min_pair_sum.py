def min_pair_sum(num: int) -> int:
    """
    Find the minimum possible sum from all pairs of digits in a four-digit number.

    Args:
        num: Four-digit integer (1000 <= num <= 9999)

    Returns:
        int: Minimum possible sum of two pairs
    """
    # Convert number to string and get individual digits
    digits = list(str(num))

    # Sort digits to easily form smallest numbers
    digits.sort()

    # Form two numbers from sorted digits
    # The optimal strategy is to pair smallest digits with smallest digits
    num1 = int(digits[0] + digits[2])  # smallest + third smallest
    num2 = int(digits[1] + digits[3])  # second smallest + largest

    # Alternative pairing
    num3 = int(digits[0] + digits[3])  # smallest + largest
    num4 = int(digits[1] + digits[2])  # second smallest + third smallest

    # Return the minimum sum
    return min(num1 + num2, num3 + num4)


def min_pair_sum_alternative(num: int) -> int:
    """
    Alternative implementation with all possible permutations.
    """
    from itertools import permutations

    digits = list(str(num))
    min_sum = float('inf')

    # Generate all permutations of digits
    for perm in permutations(digits):
        # Split into two pairs
        num1 = int(perm[0] + perm[1])
        num2 = int(perm[2] + perm[3])

        # Update minimum sum
        min_sum = min(min_sum, num1 + num2)

    return min_sum


if __name__ == '__main__':
    # Test cases
    test_cases = [2932, 4009, 1000, 9999, 1234, 3579]

    print("Testing min_pair_sum function:")
    print("-" * 40)

    for num in test_cases:
        result = min_pair_sum(num)
        result_alt = min_pair_sum_alternative(num)
        print(f"Input: {num} -> Output: {result} (Alternative: {result_alt})")

    print("\nExplanation:")
    print("2932: Possible pairs [29, 23] -> 29 + 23 = 52")
    print("4009: Possible pairs [04, 09] -> 4 + 9 = 13")