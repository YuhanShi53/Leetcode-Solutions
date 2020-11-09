""" Leetcode 470 - Implement Rand10() Using Rand7()

https://leetcode.com/problems/implement-rand10-using-rand7/

1. Rejection Sampling: Time: O(49/40)

"""

from random import randint


def rand7():
    return randint(1, 7)


class Solution1:
    """ 1. Rejection-Sampling """

    def rand10(self):
        temp = 49
        while temp >= 40:
            temp = 7 * (rand7() - 1) + rand7() - 1
        return temp % 10 + 1


if __name__ == "__main__":
    solution = Solution1()
    for i in range(10):
        print(solution.rand10())
