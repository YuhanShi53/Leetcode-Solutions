""" Leetcode 258 - Add Digits

https://leetcode.com/problems/add-digits/

1. Math Digital-Root: Time: O(1) Space: O(1)

"""


class Solution1:
    """ 1. Math Digital-Root"""

    def add_digits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1


if __name__ == '__main__':
    num = 38
    res = Solution1().add_digits(num)
    print(res)
