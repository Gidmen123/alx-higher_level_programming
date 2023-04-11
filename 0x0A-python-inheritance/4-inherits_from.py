#!/usr/bin/pythom3
"""This is the function for task 4"""


def inherits_from(obj, a_class):
    """
        This function returns True if an object is
        an instance of a subclass of a_class,
        either a specified class or inherited class,
        otherwise False.
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
