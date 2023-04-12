#!/usr/bin/python3
"""This is the function for task 8"""


class BaseGeometry():
    """
        Class BaseGeometry
    """
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        The function checks if the value passed in is an integer
        and if it is greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
