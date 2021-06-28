""" Leetcode 191 - Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/

1. Time: O(32) Memory: O(1) (32 stands for 32-bit)
2. Time: O(1) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Bit-Manipulation """

    def hamming_weight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count


class Solution2:
    """ 2. Bit-Manipulation """

    def hamming_weight(self, n):
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n


if __name__ == '__main__':
    n = 4294967293
    res = Solution1().hamming_weight(n)
    print(res)
