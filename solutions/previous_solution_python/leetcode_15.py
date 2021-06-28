""" Leetcode 15 - 3Sum

https://leetcode.com/problems/3sum/

1. self-implement - Two Pointer: Time: 2800ms Memory: 17MB
2. improved self-implement - Two Pointer: Time: 1616ms(23%) Memory: 17MB(78%)
3. Divide and Conquer: Time: 312ms(99%) Memory: 17MB(19%)

"""
from typing import List


class Solution1:
    """ 1. self-implement - Two Pointers """
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        num = len(nums)

        prev = None
        for i in range(0, num - 2):
            if prev == nums[i]:
                continue
            else:
                prev = nums[i]

            j = i + 1
            k = num - 1
            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j = self.move(j, 1, nums, i)
                elif nums[j] + nums[k] > -nums[i]:
                    k = self.move(k, -1, nums, i)
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j = self.move(j, 1, nums, i)
                    k = self.move(k, -1, nums, i)

        return res

    def move(self, idx, dx, nums, i):
        idx += dx
        while idx < len(nums) and idx > i and nums[idx] == nums[idx - dx]:
            idx += dx
        return idx


class Solution2:
    def three_sum(self, nums):
        """ 2. improved self-implement - Two Pointer """
        nums.sort()
        num = len(nums)
        res = []
        if num < 3:
            return res

        prev = None
        for i in range(0, num - 2):
            if nums[i] == prev:
                continue
            else:
                prev = nums[i]
            j = i + 1
            k = num - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
        return res


class Solution3:
    def three_sum(self, nums):
        """ 3. Divide and Conquer """
        freq = {}
        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1
        if 0 in freq and freq[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        neg = list(filter(lambda x: x < 0, freq))
        nneg = list(filter(lambda x: x >= 0, freq))
        for elem1 in neg:
            for elem2 in nneg:
                src = -(elem1 + elem2)
                if src in freq:
                    if src in (elem1, elem2) and freq[src] > 1:
                        res.append([elem1, src, elem2])
                    elif src < elem1:
                        res.append([elem1, src, elem2])
                    elif src > elem2:
                        res.append([elem1, src, elem2])
        return res


if __name__ == '__main__':
    nums = [3, 0, -2, -1, 1, 2]
    res = Solution2().three_sum(nums)
    print(res)
