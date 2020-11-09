""" Leetcode 229 - Majority Element II

https://leetcode.com/problems/majority-element-ii/


"""

from typing import List


class Solution1:
    """ 1. Boyer-Moore-Majority-Vote """

    def majority_element(self, nums: List[int]) -> List[int]:

        threshold = len(nums) / 3

        def helper(nums, ban):
            a = None
            count = 0
            for x in nums:
                if x != ban:
                    if count == 0:
                        a = x
                    elif a == x:
                        count += 1
                    elif a != x:
                        count -= 1

            count = 0
            for x in nums:
                if x == a:
                    count += 1
            if count > threshold:
                return a
            return None

        a = helper(nums, None)
        b = helper(nums, a)
        return [x for x in (a, b) if x is not None]


if __name__ == '__main__':
    nums = [0, 3, 4, 0]
    res = Solution1().majority_element(nums)
    print(res)
