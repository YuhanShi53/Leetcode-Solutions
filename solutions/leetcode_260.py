""" Leetcode 260 - Single Number III 

https://leetcode.com/problems/single-number-iii/

1. MINE Hash-Table (Space complexity not constant)
2. XOR: Time: 68ms(46%) Memory:15MB(35%)

"""

from collections import defaultdict
from functools import reduce
from typing import List


class Solution1:
    """ 1. MINE Hash-Table """

    def single_number(self, nums: List[int]) -> List[int]:
        count_dict = defaultdict(int)
        for x in nums:
            count_dict[x] += 1
        res = []
        for x in count_dict.keys():
            if count_dict[x] == 1:
                res.append(x)
        return res


class Solution2:
    """ 2. XOR """

    def single_number(self, nums):
        target_xor = reduce(lambda x, y: x ^ y, nums)
        last_one_loc = target_xor & - target_xor

        single_1 = 0
        single_2 = 0
        for x in nums:
            if x & last_one_loc:
                single_1 ^= x
            else:
                single_2 ^= x
        return [single_1, single_2]


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    res = Solution2().single_number(nums)
    print(res)
