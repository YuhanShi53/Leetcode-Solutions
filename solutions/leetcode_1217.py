""" Leetcode 1217 - Minimum Cost to Move Chips to The Same Position

https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

1. SM-CBC: Time: O(n) Space: O(1) (n is len_of_position)

"""

from typing import List


class Solution1:
    """ 1. SM-CBC """

    def min_cost_to_move_chips(self, position: List[int]) -> int:
        odd = even = 0
        for x in position:
            if x % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)


if __name__ == '__main__':
    position = [1]
    res = Solution1().min_cost_to_move_chips(position)
    print(res)
