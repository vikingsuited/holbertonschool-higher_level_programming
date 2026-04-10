#!/usr/bin/python3
"""Square (Dördbucaqlı) sinfinin tərifi."""


class Square:
    """Dördbucaqlı tərifi."""

    def __init__(self, size=0):
        """Yeni bir Square yaradır.

        Args:
            size (int): Yeni dördbucaqlının ölçüsü (susmaya görə 0).

        Raises:
            TypeError: Əgər size tam ədəd (integer) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
