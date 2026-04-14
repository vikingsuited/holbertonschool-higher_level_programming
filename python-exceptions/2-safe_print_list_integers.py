#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Siyahının ilk x elementindən tam ədəd olanları çap edir.

    Args:
        my_list: Hər hansı tipdə elementləri olan siyahı.
        x: Giriş ediləcək elementlərin sayı.

    Returns:
        Çap olunan tam ədədlərin sayı.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
