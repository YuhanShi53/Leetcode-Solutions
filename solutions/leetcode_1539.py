""" Leetcode 1539 - 

https://leetcode.com/problems/kth-missing-positive-number/

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def find_kth_positive(self, arr: List[int], k: int) -> int:
        if arr[-1] - len(arr) < k:
            return k + len(arr)

        i, j = 0, 1
        while k:
            if arr[i] == j:
                i += 1
            else:
                k -= 1
            j += 1
        return j - 1


class Solution2:
    """ 2. Binary Search """

    def find_kth_positive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return left + k


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    k = 2
    res = Solution2().find_kth_positive(arr, k)
    print(res)
