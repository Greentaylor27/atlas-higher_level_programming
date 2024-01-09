#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    if my_list is None or element is None:
        return None
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            newlist.append(element)
        newlist.append(my_list[i])
    return newlist
