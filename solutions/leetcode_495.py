""" Leetcode 495 - Teemo Attacking

https://leetcode.com/problems/teemo-attacking/


1. SM Straight-Forward: Time: O(n) Space: O(1)

"""

from typing import List


class Solution1:
    """ 1. SM Straight-Forward """

    def find_poisoned_duration(
            self, timeSeries: List[int], duration: int) -> int:

        i = 0
        total_duration = 0
        num_time = len(timeSeries)

        while i < num_time:
            start = timeSeries[i]
            end = timeSeries[i] + duration
            i += 1
            while i < num_time and timeSeries[i] < end:
                end = timeSeries[i] + duration
                i += 1
            total_duration += end - start
        return total_duration


if __name__ == '__main__':
    time_series = [1, 2]
    duration = 2
    res = Solution1().find_poisoned_duration(time_series, duration)
    print(res)
