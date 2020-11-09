""" Leetcode 342 - Power of Four

https://leetcode.com/problems/power-of-four/


"""


class Solution1:
    """ 1. SM Bit-Manipulation """

    def is_power_four(self, num: int) -> bool:
        if num > 0 and num & (num - 1) == 0 and num & 0x55555555 != 0:
            return True
        return False


if __name__ == '__main__':
    num = 8
    res = Solution1().is_power_four(num)
    print(res)
