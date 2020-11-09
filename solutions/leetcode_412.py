""" Leetcode 412 - Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

1. SM Brute-Force
2. Simiplified Brute-Force

"""

from typing import List


class Solution1:
    """ 1. SM Brute-Force """

    def fizz_buzz(self, n: int) -> List[str]:
        res = []
        for x in range(n):
            y = x + 1
            if y % 15 == 0:
                res.append("FizzBuzz")
            elif y % 5 == 0:
                res.append("Buzz")
            elif y % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(y))
        return res


class Solution2:
    """ 2. Simplified Brute-Force """

    def fizz_buzz(self, n):
        return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i)
                for i in range(1, n+1)]


if __name__ == "__main__":
    n = 15
    res = Solution2().fizz_buzz(n)
    print(res)
