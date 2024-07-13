#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Creates a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize data."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Provides the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the reactangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """This returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __del__(self):
        '''
        Detects the deletion of an instance
        and returns bye when it's deleted
        '''
        print("Bye rectangle...")

    def __str__(self):
        '''Print the rectangle with using #'''
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + '#'

                rect += '\n'
            return rect[:-1]

    def __repr__(self):
        """
        should return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
