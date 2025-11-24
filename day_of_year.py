def day_of_year(date: str) -> int:
    """
    Calculate the day of the year for a given date in format YYYY-MM-DD

    Args:
        date: String in format "YYYY-MM-DD"

    Returns:
        int: Day number of the year (1-366)
    """
    # Parse year, month, and day from the string
    year, month, day = map(int, date.split('-'))

    # Days in each month for non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  # February has 29 days in leap year

    # Calculate day of year
    day_count = 0
    for i in range(month - 1):
        day_count += days_in_month[i]

    day_count += day
    return day_count


if __name__ == '__main__':
    # Test cases
    test_data = [
        "2025-01-09",
        "2019-02-10",
        "2020-12-31",
        "2020-02-29",  # Leap year test
        "2021-03-01"  # Non-leap year test
    ]

    print("Testing day_of_year function:")
    print("-" * 30)

    for date in test_data:
        result = day_of_year(date)
        print(f"Input: {date} -> Output: {result}")