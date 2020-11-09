""" Leetcode 1103 - Distribute Candies to People

https://leetcode.com/problems/distribute-candies-to-people/


1. SM Brute-Force: Time: O(\sqrt(n)) Space: O(k) (n is num_candies, k is num_people)
2. Brute-Force: Time: O(\sqrt(n)) Space: O(k) (n is num_candies, k is num_people)

"""

from typing import List


class Solution1:
    """ 1. SM Brute Force"""

    def distribute_candies(self, candies: int, num_people: int) -> List[int]:
        distribution = [0 for i in range(num_people)]
        idx = 0
        while candies > 0:
            row_idx = idx // num_people
            col_idx = idx % num_people
            temp = col_idx + 1 + row_idx * num_people
            distribution[col_idx] += temp
            candies -= temp
            idx += 1
        distribution[col_idx] += candies
        return distribution


class Solution2:
    """ 2. Brute-Force """

    def distribute_candies(self, candies, num_people):
        distribution = [0] * num_people
        idx = 0
        while candies > 0:
            distribution[idx % num_people] += min(candies, idx+1)
            candies -= idx + 1
            idx += 1
        return distribution


if __name__ == '__main__':
    candies = 10
    num_people = 3
    res = Solution2().distribute_candies(candies, num_people)
    print(res)
