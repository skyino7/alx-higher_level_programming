#!/usr/bin/python3

"""
Write a function that divides
element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            new = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            new = 0
        except ZeroDivisionError:
            print("division by 0")
            new = 0
        except IndexError:
            print("out of range")
            new = 0
        finally:
            new_list.append(new)

    return new_list
