#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    l, h = 0, len(list_of_integers) - 1

    while l < h:
        mid = (l + h) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            h = mid
        else:
            l = mid + 1

    return list_of_integers[l]
