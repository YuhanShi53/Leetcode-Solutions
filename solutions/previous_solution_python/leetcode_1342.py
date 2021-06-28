""" Leetcode 1342 - Number of Steps to Reduce a Number to Zero

https: // leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

1. Time: O(1) Memory: O(1)
2. Time: O(1) Memory: O(1)

"""


class Solution1:
    """ 1. MINE | Bit-Manipulation """

    def number_of_steps(self, num: int) -> int:
        step = len(bin(num)) - 3
        while num:
            num &= (num - 1)
            step += 1
        return step


class Solution2:
    """ 2. Bit-Manipulation """

    def number_of_steps(self, num):
        return len(bin(num)) + bin(num).count('1') - 3


if __name__ == '__main__':
    num = 8
    step = Solution1().number_of_steps(num)
    print(step)
