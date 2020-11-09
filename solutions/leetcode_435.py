""" Leetcode 435 - Non-Overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/


"""

from typing import List


class Solution1:
    """ 1. SM """

    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 0
        threshold = intervals[0][0]

        for low, high in intervals:
            if low < threshold:
                count += 1
            else:
                threshold = high
        return count


if __name__ == '__main__':
    intervals = []
    res = Solution1().erase_overlap_intervals(intervals)
    print(res)
