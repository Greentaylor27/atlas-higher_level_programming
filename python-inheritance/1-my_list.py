#!/usr/bin/python3
"""Class known as MyList"""


class MyList(list):
    """Child class for what I assume is list"""


    def print_sorted(self):
        """Method that should sort list"""
        SortedList = sorted(self)
        print(SortedList)
