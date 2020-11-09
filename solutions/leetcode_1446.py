""" Leetcode 1446 - Consecutive Characters

https://leetcode.com/problems/consecutive-characters/

1. SM Straight-Forward: Time: O(N) Space: O(1) (N is len_of_s)
2. Python-Method: Time: O(N) Space: O(N) (N is len_of_s)

"""


class Solution1:
    """ 1. SM Straight-Forward """

    def max_power(self, s: str) -> int:
        max_power = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                max_power = max(max_power, count)
            else:
                count = 1
        return max_power


class Solution2:
    """ 2. Python-Method """

    def max_power(self, s):
        from itertools import groupby
        return max(len(list(y)) for _, y in groupby(s))


if __name__ == '__main__':
    s = "leetcode"
    res = Solution2().max_power(s)
    print(res)
