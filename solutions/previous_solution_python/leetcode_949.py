""" Leetcode 949 - Largest Time for Given Digits

https://leetcode.com/problems/largest-time-for-given-digits/

1. MINE BFS: Time: O(24) Space: O(24)

"""

from typing import List


class Solution1:
    """ 1. MINE BFS """

    def largest_time_from_digits(self, A: List[int]) -> str:
        A.sort(reverse=True)

        def bfs(nums, x, factor):
            if not nums:
                return x if x <= 2359 and x % 100 < 60 else ''
            for i, y in enumerate(nums):
                new_x = x + y * factor
                if new_x <= 2359:
                    temp = bfs(nums[:i] + nums[i+1:], new_x, factor // 10)
                    if isinstance(temp, int):
                        return temp

        x = bfs(A, 0, 1000)
        if isinstance(x, int):
            return '{:02d}:{:02d}'.format(x//100, x % 100)
        else:
            return ''


if __name__ == '__main__':
    nums = [1, 9, 6, 0]
    res = Solution1().largest_time_from_digits(nums)
    print(res)
