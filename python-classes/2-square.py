#!/usr/bin/python3
"""Square class modulunu təsvir edir."""


class Square:
    """Kvadrat sinfi."""

    def __init__(self, size=0):
        """Kvadratı yaradarkən ölçünü yoxlayıb təyin edir."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2
