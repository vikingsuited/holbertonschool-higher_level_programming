#!/usr/bin/python3
"""Square (Dördbucaqlı) sinfinin tərifi."""


class Square:
    """Dördbucaqlı tərifi."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni bir Square yaradır.

        Args:
            size (int): Ölçü.
            position (tuple): Koordinat (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Position setter."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Dördbucaqlını koordinatlara uyğun # ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y koordinatı (şaquli boşluqlar)
        [print("") for i in range(self.__size_position[1])]

        for i in range(self.__size):
            # X koordinatı (üfüqi boşluqlar)
            print(" " * self.__size_position[0], end="")
            print("#" * self.__size)
