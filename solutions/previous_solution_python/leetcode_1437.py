""" Leetcode 1437 - Check If All 1s Are at Least K Places Away

https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


1. Time: O(n) Memory: O(1) (n is length of nums)

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def k_length_apart(self, nums: List[int], k: int) -> bool:
        prev = -k - 1
        for i, x in enumerate(nums):
            if x == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True


if __name__ == '__main__':
    nums = [1]
    k = 1
    res = Solution1().k_length_apart(nums, k)
    print(res)
