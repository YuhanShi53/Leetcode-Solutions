""" Leetcode 1658 - Minimum Operations to Reduce x to Zero

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

1. Time: O(N) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE | Two-Pointers """

    def min_operations(self, nums: List[int], x: int) -> int:
        residual = sum(nums) - x
        if residual < 0:
            return -1
        if residual == 0:
            return len(nums)
        idx, sum_x, max_length = 0, 0, 0
        for i, x in enumerate(nums):
            sum_x += x
            while sum_x > residual:
                sum_x -= nums[idx]
                idx += 1
            if sum_x == residual:
                max_length = max(max_length, i - idx + 1)
        return len(nums) - max_length if max_length else -1


if __name__ == '__main__':
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    res = Solution1().min_operations(nums, x)
    print(res)
