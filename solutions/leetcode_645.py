""" Leetcode 645 - Set Mismatch

https://leetcode.com/problems/set-mismatch/

1. Time: O(n) Memory: O(n)
2. Time: O(n) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE | Straight-Forward """

    def find_error_nums(self, nums: List[int]) -> List[int]:
        count = [0 for i in range(len(nums))]
        for x in nums:
            count[x-1] += 1
        a, b = None, None
        for i, x in enumerate(count):
            if x == 0:
                b = i + 1
            elif x == 2:
                a = i + 1
        return [a, b]


class Solution2:
    """ 2. Improvement on 1 | Inplace """

    def find_error_nums(self, nums):
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res


if __name__ == '__main__':
    nums = [3, 2, 2]
    res = Solution2().find_error_nums(nums)
    print(res)
