""" Leetcode 1041 - Robot Bounded in Circle

https://leetcode.com/problems/robot-bounded-in-circle/


"""


class Solution1:
    """ 1. MINE Straight-Forward """

    def is_robot_bounded(self, instructions: str) -> bool:
        nums = {'G': 0, 'R': 1, 'L': -1}
        direction = [1, -1]
        position = [0, 0]
        idx = 0
        summation = 0
        factor = 1

        for x in instructions:
            summation += nums[x]
            if x in ('R', 'L'):
                idx = 1 - idx
                factor *= nums[x] * direction[idx]
            else:
                position[idx] += factor * 1

        if summation % 4 == 0 and position != [0, 0]:
            return False
        return True


if __name__ == '__main__':
    instructions = "GGG"
    res = Solution1().is_robot_bounded(instructions)
    print(res)
