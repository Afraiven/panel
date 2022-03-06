import datetime

from stdnum.exceptions import *
from stdnum.util import clean, isdigits


def compact(number):
    """Convert the number to the minimal representation. This strips the
    number of any valid separators and removes surrounding whitespace."""
    return clean(number, ' -').upper().strip()


def get_birth_date(number):
    """Split the date parts from the number and return the birth date."""
    number = compact(number)
    year = int(number[0:2])
    month = int(number[2:4])
    day = int(number[4:6])
    year += {
        0: 1900,
        1: 2000,
        2: 2100,
        3: 2200,
        4: 1800,
    }[month // 20]
    month = month % 20
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise InvalidComponent()


def get_gender(number):
    """Get the person's birth gender ('M' or 'F')."""
    number = compact(number)
    if number[9] in '02468':  # even
        return 'F'
    else:  # odd: 13579
        return 'M'


def calc_check_digit(number):
    """Calculate the check digit for organisations. The number passed
    should not have the check digit included."""
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    check = sum(w * int(n) for w, n in zip(weights, number))
    return str((10 - check) % 10)


def validate(number):
    """Check if the number is a valid national identification number. This
    checks the length, formatting and check digit."""
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) != 11:
        raise InvalidLength()
    if number[-1] != calc_check_digit(number[:-1]):
        raise InvalidChecksum()
    get_birth_date(number)
    return number


def is_valid(number):
    """Check if the number is a valid national identification number."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False
