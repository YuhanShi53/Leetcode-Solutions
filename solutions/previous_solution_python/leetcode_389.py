""" Leetcode 389 - Find the difference

https://leetcode.com/problems/find-the-difference/

1. MINE Hash: Time: O(n) Space: O(n) (n is len_s)
2. MINE Bit-Manipulation: Time: O(n) Space: O(1) (n is len_s)

"""


class Solution1:
    """ 1. MINE Hash """

    def find_the_difference(self, s: str, t: str) -> str:
        words = {}
        for x in t:
            words[x] = words.get(x, 0) + 1
        for x in s:
            words[x] -= 1
        for key, value in words.items():
            if value == 1:
                return key


class Solution2:
    """ 2. MINE Bit-Manipulation """

    def find_the_difference(self, s, t):
        difference = 0
        for x in s + t:
            difference ^= ord(x)
        return chr(difference)


if __name__ == '__main__':
    s = 'abcd'
    t = 'abcde'
    res = Solution2().find_the_difference(s, t)
    print(res)
