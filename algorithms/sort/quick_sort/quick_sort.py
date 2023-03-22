from typing import List


def quick_sort(array: List[int], is_descend: bool = False) -> None:

    def partition(low, high, v) -> int:
        left, right = low+1, high
        while True:
            while array[left] < v:
                left += 1
                if (left == high):
                    break
            while array[right] > v:
                right -= 1
                if (right == low):
                    break
            if left >= right:
                break
            array[left], array[right] = array[right], array[left]
        array[low], array[right] = array[right], array[low]

        return right

    def quick_sort_helper(low, high):
        if low >= high:
            return
        j = partition(low, high, array[low])
        quick_sort_helper(low, j-1)
        quick_sort_helper(j+1, high)

    quick_sort_helper(0, len(array)-1)
    if is_descend:
        array.reverse()
