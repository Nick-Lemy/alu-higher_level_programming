#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Creates a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize data."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size
        '''
        return cls(size, size)

    def __del__(self):
        '''
        Detects the deletion of an instance
        and returns bye when it's deleted
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        '''Print the rectangle with using #'''
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + str(self.print_symbol)

                rect += '\n'
            return rect[:-1]

    def __repr__(self):
        """
        should return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
