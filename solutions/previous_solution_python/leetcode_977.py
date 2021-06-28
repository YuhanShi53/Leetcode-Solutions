""" Leetcode 977 - Squares of a sorted array

https://leetcode.com/problems/squares-of-a-sorted-array/

1. Time: O(n) Memory: O(n) (n is length of nums)
2. Time: O(n) Memory: O(n) (n is length of nums)
3. Time: O(n) in this case, normally is O(nlogn) Memory: O(n) (n is length of nums)

"""

from typing import List


class Solution1:
    """ 1. Mine """

    def sorted_square(self, nums: List[int]) -> List[int]:
        for th, x in enumerate(nums):
            if x >= 0:
                break
        res = []
        i, j = th - 1, th
        while i > -1 and j < len(nums):
            if nums[i] ** 2 <= nums[j] ** 2:
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1
        while i > -1:
            res.append(nums[i] ** 2)
            i -= 1
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1
        return res


class Solution2:
    """ 2. Two-Pointer """

    def sorted_square(self, nums):
        start, end = 0, len(nums) - 1
        sorted_nums = []
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                sorted_nums.insert(0, nums[start] ** 2)
                start += 1
            else:
                sorted_nums.insert(0, nums[end] ** 2)
                end -= 1
        return sorted_nums


class Solution3:
    """ 3. TimSort """

    def sorted_square(self, nums):
        return sorted([x**2 for x in nums])


if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    res = Solution3().sorted_square(nums)
    print(res)
