#!/usr/bin/python3
"""define a rectangle."""


class Rectangle:
    """represent rectangle."""

    def width(self, value):
        """Initilize a new width.

        Args: value (int): the width of the new rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.width = value
    def height(sel, value):
        """Initilize a new height.

        Args: value (int): the height of a new rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.height = value





