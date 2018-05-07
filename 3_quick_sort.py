"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    lo, hi = 0, len(array) - 1
    print(lo, hi, array)
    pivot = array[hi]
    while lo < hi:
        if array[lo] >= pivot:
            tmp = array[lo]
            array[lo] = array[hi-1]
            array[hi-1] = pivot
            array[hi] = tmp
            hi = hi - 1
        else:
            lo += 1
    return quicksort(array[:hi]) + quicksort(array[hi:])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)