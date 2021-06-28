""" Leetcode 50 - Pow(x, n)

https://leetcode.com/problems/powx-n/

1. self-implement: Time: 36ms(37%) Memory: 14MB(11%)
2. Iterative Bit-mannipulation: Time: 40ms(30%) Memory: 13.9MB(46%)

"""


class Solution1:
    """ 1. self-implement """
    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
        n = abs(n)

        total_res = 1
        current_res = x
        current_pow = 1

        while n > 0:
            if current_pow * 2 > n:
                n -= current_pow
                total_res *= current_res
                current_pow = 1
                current_res = x
            else:
                current_pow *= 2
                current_res *= current_res
        return total_res


class Solution2:
    """ 2. Iterative Bit-Manipulation """
    def my_pow(self, x, n):
        if n == 0:
            return 1

        abs_n = abs(n)
        res = 1
        while abs_n:
            if abs_n % 2:
                res *= x
            x *= x
            abs_n >>= 1
        return res if n > 0 else 1 / res


if __name__ == '__main__':
    x = 2.1
    n = 3
    res = Solution1().my_pow(x, n)
    print(res)
