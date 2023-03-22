from typing import List


def merge_sort(array: List[int], is_descend: bool = False) -> None:
    """Space Complexity: O(n)
    """
    assistance_array = [0] * len(array)

    def merge_sort_helper(start, end):
        if end - start == 1:
            return
        mid = start + (end - start) // 2
        merge_sort_helper(start, mid)
        merge_sort_helper(mid, end)

        for i in range(start, end):
            assistance_array[i] = array[i]
        idx = start
        mid_copy = mid
        while start < mid_copy and mid < end:
            if (assistance_array[start] > assistance_array[mid]) ^ is_descend:
                array[idx] = assistance_array[mid]
                mid += 1
            else:
                array[idx] = assistance_array[start]
                start += 1
            idx += 1

        if start < mid_copy:
            array[idx:end] = assistance_array[start:mid_copy]
        else:
            array[idx:end] = assistance_array[mid:end]

    merge_sort_helper(0, len(array))
