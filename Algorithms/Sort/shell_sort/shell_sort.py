from typing import List


def shell_sort(array: List[int], is_descend: False):
    gap = len(array) // 2
    while gap > 0:
        for i in range(len(array) - gap, len(array)):
            key = array[i]
            j = i - gap
            while j >= 0 and ((array[j] > key) ^ is_descend):
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = key
        gap //= 2
