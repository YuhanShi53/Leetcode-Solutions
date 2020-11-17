""" Leetcode 858 - Mirror Reflection

https://leetcode.com/problems/mirror-reflection/

"""


class Solution1:
    """ 1. MINE-Math """

    def mirror_reflection(self, p: int, q: int) -> int:
        def greatest_common_divisor(x, y):
            if y > x:
                x, y = y, x
            while x % y != 0:
                x, y = y, x % y
            return y

        least_common_multiple = p * q // greatest_common_divisor(p, q)

        num_horizontal_reflect = least_common_multiple // q % 2
        num_vertial_reflect = least_common_multiple // p % 2

        targets = {(0, 1): 0, (1, 1): 1, (1, 0): 2}
        return targets[(num_vertial_reflect, num_horizontal_reflect)]


class Solution2:
    def mirror_reflection(self, p: int, q: int):
        while p % 2 and q % 2:
            p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2


if __name__ == '__main__':
    p = 4
    q = 3
    res = Solution1().mirror_reflection(p, q)
    print(res)
