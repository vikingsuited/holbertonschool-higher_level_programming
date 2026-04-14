#!/usr/bin/python3
def safe_print_integer(value):
    """Tam ədədi təhlükəsiz şəkildə çap edən funksiya.

    Args:
        value: Hər hansı bir tipdə olan dəyər.

    Returns:
        True əgər çap uğurludursa, əks halda False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
