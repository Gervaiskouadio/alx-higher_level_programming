#!/usr/bin/python3
"""define a rectangle."""


class Rectangle:
    """represent rectangle."""

    def width(self, width):
        """Initilize a new width.

        Args: width (int): the width of the new rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
    def height(sel, height):
        """Initilize a new height.

        Args: height (int): the height of a new rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.height = height





