""" Leetcode 575 - Distribute Candies

https://leetcode.com/problems/distribute-candies/

"""

from typing import List


class Solution1:
    """ 1. MINE | Set """

    def distribute_candies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)


if __name__ == '__main__':
    candies = [1, 2]
    res = Solution1().distribute_candies(candies)
    print(res)
