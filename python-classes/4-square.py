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
        """Ölçünü götürmək üçün getter (retrieve).

        Returns:
            Dördbucaqlının ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin etmək üçün setter.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Dördbucaqlının sahəsini hesablayır.

        Returns:
            Dördbucaqlının sahəsi.
        """
        return self.__size ** 2
