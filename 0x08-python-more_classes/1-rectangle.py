#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods for getting and setting them"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle,
        while validating that it is an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle,
        while validating that it is an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
