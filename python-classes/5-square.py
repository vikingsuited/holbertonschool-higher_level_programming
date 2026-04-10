#!/usr/bin/python3
"""Square (Dördbucaqlı) sinfinin tərifi."""


class Square:
    """Dördbucaqlı tərifi."""

    def __init__(self, size=0):
        """Yeni bir Square yaradır.

        Args:
            size (int): Yeni dördbucaqlının ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Ölçünü götürmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Dördbucaqlını # simvolları ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
