from typing import List


def selection_sort(array: List[int], is_descend: bool = False):
    for i in range(len(array)):
        selection = i
        for j in range(i+1, len(array)):
            if (array[selection] > array[j]) ^ is_descend:
                selection = j
        array[selection], array[i] = array[i], array[selection]
