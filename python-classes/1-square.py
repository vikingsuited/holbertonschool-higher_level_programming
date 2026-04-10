#!/usr/bin/python3
"""Square (Dördbucaqlı) sinfinin tərifi."""


class Square:
    """Dördbucaqlı tərifi."""

    def __init__(self, size):
        """Yeni bir Square yaradır.

        Args:
            size (int): Yeni dördbucaqlının ölçüsü.
        """
        self.__size = size
