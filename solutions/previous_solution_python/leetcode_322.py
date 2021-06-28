""" Leetcode 322 - Coin Change

https://leetcode.com/problems/coin-change/

1. Time: O(n*amount) Memory: O(amount)
2. Time: O(n*amount) Memory: O(amount)
3. Time: Pending...

"""

from typing import List


class Solution1:
    """ 1. Dynamic Programming

    Borrow from: https://leetcode.com/problems/coin-change/discuss/77360/C%2B%2B-O(n*amount)-time-O(amount)-space-DP-solution

    """

    def coin_change(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] + [amount+1] * amount
        for i in range(1, amount+1):
            dp[i] = min(
                [dp[i-x] + 1 if i >= x else amount + 1 for x in coins])
        return -1 if dp[amount] > amount else dp[amount]


class Solution2:
    """ 2. BFS

    Borrow from: https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution

    """

    def coin_change(self, coins, amount):
        if amount == 0:
            return 0
        values = [0]
        temp = []
        visited = [True] + [False] * amount
        count = 0
        while values:
            count += 1
            for value in values:
                for coin in coins:
                    if value + coin == amount:
                        return count
                    if value + coin > amount:
                        continue
                    elif not visited[value+coin]:
                        visited[value+coin] = True
                        temp.append(value+coin)
            values, temp = temp, []
        return -1


class Solution3:
    """ 3. DFS """

    def coin_change(self, coins, amount):
        coins.sort(reverse=True)
        THRESHOLD = 10 ** 4 + 1
        count = THRESHOLD

        def helper(total, current_count, idx):
            nonlocal count
            if total == amount:
                count = min(count, current_count)
            if idx < len(coins):
                if coins[idx] <= amount < total + coins[idx] * (count - current_count):
                    for x in range(1, min(count-current_count, (amount-total)//coins[idx])+1):
                        helper(total+x*coins[idx], current_count+x, idx+1)
                helper(total, current_count, idx+1)

        helper(0, 0, 0)
        return -1 if count == THRESHOLD else count


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    res = Solution3().coin_change(coins, amount)
    print(res)
