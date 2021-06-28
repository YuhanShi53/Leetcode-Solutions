""" Leetcode 421 - Maximum XOR of Two Numbers in an Array

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/


"""

from typing import List


class Solution1:
    """ 1. Trie """

    def find_maximum_xor(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        trie = {}
        for x in nums:
            node = trie
            for i in range(31)[::-1]:
                bit = (x >> i) & 1
                if bit in node:
                    node = node[bit]
                else:
                    node[bit] = {}
                    node = node[bit]

        maximum_xor = -2**31
        for x in nums:
            temp = 0
            node = trie
            for i in range(31)[::-1]:
                bit = (x >> i) & 1
                if 1 - bit in node.keys():
                    temp += 2 ** i
                    node = node[1 - bit]
                else:
                    node = node[bit]
            maximum_xor = max(maximum_xor, temp)
        return maximum_xor


if __name__ == '__main__':
    nums = []
    res = Solution1().find_maximum_xor(nums)
    print(res)
