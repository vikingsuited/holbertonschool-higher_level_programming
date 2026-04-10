#!/usr/bin/python3
"""Square (Dördbucaqlı) sinfinin tərifi."""


class Square:
    """Dördbucaqlı tərifi."""

    def __init__(self, size=0):
        """Yeni bir Square yaradır.

        Args:
            size (int): Yeni dördbucaqlının ölçüsü.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Dördbucaqlının sahəsini hesablayır.

        Returns:
            Dördbucaqlının sahəsi (int).
        """
        return self.__size ** 2
