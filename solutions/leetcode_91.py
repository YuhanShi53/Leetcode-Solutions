""" Leetcode 91 - Decode Ways

https://leetcode.com/problems/decode-ways/

1. Time: O(n) Memory: O(1) (n is length of s)

"""


class Solution1:
    """ 1. MINE | DP """

    def num_decodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        prev = prev2 = 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] > '0':
                temp += prev
            if '10' <= s[i-1:i+1] <= '26':
                temp += prev2
            prev, prev2 = temp, prev
        return prev


if __name__ == '__main__':
    s = '226'
    res = Solution1().num_decodings(s)
    print(res)
