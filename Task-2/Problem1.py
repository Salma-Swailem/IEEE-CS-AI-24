def is_leap_year(year):
    """
    Check if given year is a leap year

    A leap year is either:
    Divisible by 4 but not by 100,
    or Divisible by 400

    Parameters:
    year (int): The year to be checked

    Returns:
    bool: True if the year is a leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


try:
    year = int(input('Enter a year: '))
    print(is_leap_year(year))
except ValueError:
    print('\nInvalid input')
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
