from typing import List


def bubble_sort(array: List[int], is_descend: bool = False):
    length = len(array)
    for i in range(length):
        is_sorted = True
        for j in range(1, length - i):
            if (array[j-1] > array[j]) ^ is_descend:
                array[j-1], array[j] = array[j], array[j-1]
                is_sorted = False
        if is_sorted:
            return
