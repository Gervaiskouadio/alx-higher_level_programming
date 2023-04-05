#!/usr/bin/python3
#1-rectangle.py
"""function that defines the width and the height of a rectangle."""


class Rectangle:
    """represent rectangle."""

    def __init__(self, width=0, height=0)
        """Initilize a new width and height.

        Args: width (int): the width of the new rectangle.
            height (int): the height of a new rectangle.
        """
        self.width = width
        sel.height = height

    @property
    def width(self):
        """Get the current width of the rectngle."""
        return (self.__width)

    @width.setter
    def width(sel, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property 
    def height(self):
        """get the current height of a rectangle"""
        return (self.__height)
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
