""" Leetcode 983 - Minimum Cost for Tickets

https://leetcode.com/problems/minimum-cost-for-tickets/

"""

from collections import deque
from typing import List


class Solution1:
    """ 1. MINE """

    def min_cost_ticket(self, days: List[int], costs: List[int]) -> int:
        min_cost = [0 for x in range(365 + 30)]
        idx = 30
        while days:
            current_day = idx - 29
            if current_day == days[0]:
                days.remove(current_day)
                min_cost[idx] = min(min_cost[idx-1] + costs[0],
                                    min_cost[idx-7] + costs[1],
                                    min_cost[idx-30] + costs[2])
            else:
                min_cost[idx] = min_cost[idx - 1]
            idx += 1
        return min_cost[idx - 1]


class Solution2:
    """ 2. DP """

    def min_cost_ticket(self, days, costs):
        last_7 = deque()
        last_30 = deque()
        cost = 0

        for day in days:
            while last_7 and last_7[0][0] + 7 <= day:
                last_7.popleft()
            while last_30 and last_30[0][0] + 30 <= day:
                last_30.popleft()
            last_7.append((day, cost))
            last_30.append((day, cost))
            cost = min(cost + costs[0],
                       last_7[0][1] + costs[1],
                       last_30[0][1] + costs[2])
        return cost


if __name__ == '__main__':
    days = [365]
    costs = [2, 7, 15]
    res = Solution2().min_cost_ticket(days, costs)
    print(res)
