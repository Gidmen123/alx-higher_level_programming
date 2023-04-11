#!/usr/bin/python3
""" THis function creates a class for task 1"""


class MyList(list):
    """
        This class inherits all the methods and attributes
        of the list class and
        sorts the list in ascending order
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        """
            This function returns the sorted list
        """
        print(sorted_list)
