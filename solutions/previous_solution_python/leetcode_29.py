""" Leetcode 29 - Divede Two Integerss

https://leetcode.com/problems/divide-two-integers/

1. Time: O(logn^2) Memory: O(1)
2. Time: O(32) Memory: O(1)

"""


class Solution1:
    """ 1. Math """

    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == 11:
            return 2**31-1
        factor = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            count = 1
            divisor_cp = divisor
            while dividend >= divisor_cp * 2:
                divisor_cp <<= 1
                count <<= 1
            dividend -= divisor_cp
            res += count
        return res * factor


class Solution2:
    """ 2. Bit-Manipulation """

    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == 11:
            return 2**31-1
        factor = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0
        while dividend >= divisor:
            for x in range(32)[::-1]:
                if dividend >> x >= divisor:
                    dividend -= divisor << x
                    count += 1 << x
        return count * factor


if __name__ == "__main__":
    dividend = -17
    divisor = 3
    res = Solution2().divide(dividend, divisor)
    print(res)
