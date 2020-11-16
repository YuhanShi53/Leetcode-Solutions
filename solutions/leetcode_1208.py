""" Leetcode 1208 - Get Equal Substrings within Budget

https://leetcode.com/problems/get-equal-substrings-within-budget/

1. MINE Two-pointer: Time: O(n) Space: O(n)
2. Sliding-Window: Time: O(n) Space: O(1)

"""


class Solution1:
    """ 1. MINE Two-pointer """

    def equal_substring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        for x, y in zip(s, t):
            costs.append(abs(ord(x) - ord(y)))

        low, high = -1, -1
        total_cost = 0
        max_len = 0
        while high < len(costs) - 1:
            if total_cost <= maxCost or low == high:
                high += 1
                total_cost += costs[high]
            else:
                low += 1
                total_cost -= costs[low]

            if total_cost <= maxCost:
                max_len = max(max_len, (high-low))

        return max_len


class Solution2:
    """ 2. Sliding-Window """

    def equal_substring(self, s, t, maxCost):
        i = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1


if __name__ == '__main__':
    s = "krpgjbjjznpzdfy"
    t = "nxargkbydxmsgby"
    max_cost = 14
    res = Solution2().equal_substring(s, t, max_cost)
    print(res)
