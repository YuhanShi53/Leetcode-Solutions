""" Leetcode 1679 - Max Number of K Sum Pairs

https://leetcode.com/problems/max-number-of-k-sum-pairs/


"""

from typing import List


class Solution1:
    """ 1. MINE | Hash """

    def max_operations(self, nums: List[int], k: int) -> int:
        count = 0
        num_dict = {}
        for x in nums:
            if num_dict.get(x, None) is None:
                num_dict[x] = 0
            num_dict[x] += 1
        for x in num_dict.keys():
            if x < k:
                if x == k / 2:
                    count += num_dict[x] // 2
                    num_dict[x] = 0
                elif num_dict.get(k - x, 0) > 0:
                    count += min(num_dict[x], num_dict[k-x])
                    num_dict[x], num_dict[k - x] = 0, 0
        return count


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    k = 5
    res = Solution1().max_operations(nums, k)
    print(res)
