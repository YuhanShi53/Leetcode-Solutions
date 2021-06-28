""" Leetcode 881 - Boats to Save People

https://leetcode.com/problems/boats-to-save-people/

1. Time: O(nlogn) Memory: O(1)
2. Time: O(nlogn) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE | Sort | Two-Pointers """

    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, count = 0, len(people) - 1, 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            count += 1
        return count


class Solution2:
    """ 2. Simplified of 1 """

    def num_rescue_boats(self, people, limit):
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
        return left


if __name__ == '__main__':
    people = [3, 2, 2, 1]
    limit = 3
    res = Solution1().num_rescue_boats(people, limit)
    print(res)
