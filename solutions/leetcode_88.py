""" Leetcode 88 - Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

 1. Time: O(m+n) Space: O(1) (m, n are length of nums1 and nums2)
 2. Time: O(m+n) Space: O(1) (m, n are length of nums1 and nums2)

"""

from typing import List


class Solution1:
    """ 1. MIME """

    def merge(
            self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]


class Solution2:
    """ 2. Simplified of 1 """

    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution2().merge(nums1, m, nums2, n)
    print(nums1)
