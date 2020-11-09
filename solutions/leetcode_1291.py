""" Leetcode 1291 - Sequential Digits

https://leetcode.com/problems/sequential-digits/


"""


from typing import List


class Solution1:
    """ 1. SM Straight-Forward """

    def sequential_digits(self, low: int, high: int) -> List[int]:
        short_len = len(str(low))
        long_len = len(str(high))
        candidates = []

        for i in range(short_len, long_len+1):
            for j in range(1, 11-i):
                x = 0
                for k in range(i):
                    x = x * 10 + j
                    j += 1
                if low <= x <= high:
                    candidates.append(x)
                if x > high:
                    return candidates
        return candidates


if __name__ == '__main__':
    low = 234
    high = 2314
    res = Solution1().sequential_digits(low, high)
    print(res)
