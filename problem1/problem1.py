def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year.

    A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to check

    Returns:
    bool: True if the year is a leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
