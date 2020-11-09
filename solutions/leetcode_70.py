""" Leetcode 70 - Climbing Stairs

https://leetcode.com/problems/climbing-stairs/

1. SM DP: Time: O(n) Space: O(1)

"""


class Solution1:
    """ 1. SM DP """

    def climb_stairs(self, n: int) -> int:
        s1, s2 = 1, 0
        while n:
            s1, s2 = s1 + s2, s1
            n -= 1
        return s1


if __name__ == "__main__":
    n = 2
    res = Solution1().climb_stairs(n)
    print(res)
