""" Leetcode 1663 - Smallest String With A Given Numeric Value

https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

1. Time: O(n) Memory: O(n)
2. Time: O(1) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Greedy """

    def get_smallest_string(self, n: int, k: int) -> str:
        string = [1 for i in range(n)]
        k -= n
        n -= 1
        while k:
            d = min(k, 25)
            string[n] += d
            k -= d
            n -= 1
        return ''.join([chr(96+x) for x in string])


class Solution2:
    """ 2. Greedy """

    def get_smallest_string(self, n, k):
        k -= n
        num_z = k // 25
        if num_z == n:
            return 'z' * n
        num_a = n - num_z - 1
        residual = k - num_z * 25
        return 'a' * num_a + chr(residual+97) + 'z' * num_z


if __name__ == '__main__':
    n = 5
    k = 73
    res = Solution2().get_smallest_string(n, k)
    print(res)
