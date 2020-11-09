""" Leetcode 134 - Gas Station

https://leetcode.com/problems/gas-station/


1. SM Straight-Forward: Time: O(n) Space: O(1)
2. Greedy: Time: O(n) Space: O(1)

"""

from typing import List


class Solution1:
    """ 1. SM Straight-Forward """

    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        total_profit = 0
        current_profit = -1
        candidate = None

        for i, (x, y) in enumerate(zip(gas, cost)):
            if current_profit < 0 and (x - y) >= 0:
                candidate = i
                current_profit = x - y
            elif current_profit >= 0:
                current_profit += x - y
            total_profit += x - y
        if total_profit >= 0:
            return candidate
        return -1


class Solution2:
    """ 2. Greedy """

    def can_complete_circuit(self, gas, cost):
        start = len(gas) - 1
        end = 0
        total_profit = gas[start] - cost[start]
        while start > end:
            if total_profit >= 0:
                total_profit += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                total_profit += gas[start] - cost[start]
        return start if total_profit >= 0 else -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    res = Solution2().can_complete_circuit(gas, cost)
    print(res)
