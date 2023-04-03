#!/usr/bin/python3
"""Defining a Rectangle"""

class Rectangle:
    """define Rectangle"""
    def __init__(self, width=0, height=0):
        """initializing Rectangle
        Args:
        width(int): width of Rectangle
        height(int): height of Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """initialize width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        if not isinstance(valie, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defining area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter (self):
        """Define perimeter of Rectangle
            represent with '#'
        """
        if width == 0 or height == 0:
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))
