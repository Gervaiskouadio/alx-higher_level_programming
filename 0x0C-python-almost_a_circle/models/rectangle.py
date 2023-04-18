#!/usr/bin/python3
#rectangle.py

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0,id=None):

        super()__init__(id)
        self.width = width
        sel.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("value must be integer")
        if value <= 0:
            raise ValueError ("value must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError ("value must be integer")
        if value <= 0:
            raise ValueError ("value must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError ("value must be integer")
        if value < 0:
            raise ValueError ("value must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError ("value must be integer")
        if value < 0:
            raise ValueError ("value must be >= 0")
        self.__y = value
    
    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

     def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
