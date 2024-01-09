#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None or element is None:
        return None
    my_list.insert(idx, element)
    return my_list
