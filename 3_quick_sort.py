"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, low, high):
    pivot = array[high]
    while low < high:
        if array[low] >= pivot:
            tmp = array[low]
            array[low] = array[high-1]
            array[high-1] = pivot
            array[high] = tmp
            high = high - 1
        else:
            low += 1
    return high

def _quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        _quicksort(array, low, pi - 1)
        _quicksort(array, low + 1, high)

def quicksort(array):
    lo, hi = 0, len(array) - 1
    _quicksort(array, lo, hi)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)