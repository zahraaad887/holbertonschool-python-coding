#!/usr/bin/python3
"""Square class modulunu təsvir edir."""


class Square:
    """Kvadrat sinfi."""

    def __init__(self, size=0):
        """Kvadratı yaradarkən ölçünü yoxlayıb təyin edir."""
        self.size = size

    @property
    def size(self):
        """Ölçünü oxumaq (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü dəyişmək (setter)."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' ilə çapa verir."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
