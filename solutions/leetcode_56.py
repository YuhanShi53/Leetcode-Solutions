""" Leetcode 56 - Merge Intervals

https://leetcode.com/problems/merge-intervals/

1. Time: O(NlogN) Memory: O(N) (N is length of intervals)
2. Time: O(NlogN) Memory: O(N) (N is length of intervals)

"""

from typing import List


class Solution1:
    """ 1. MINE-Sort """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        merged_intervals = []
        for i, j in intervals:
            if i <= end:
                end = max(end, j)
            else:
                merged_intervals.append([start, end])
                start, end = i, j
        merged_intervals.append([start, end])
        return merged_intervals


class Solution2:
    """
    2. Improvement-of-1

    https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python
    """

    def merge(self, intervals):
        merged_intervals = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if merged_intervals and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(
                    merged_intervals[-1][1], interval[1])
            else:
                merged_intervals += interval,
        return merged_intervals


if __name__ == '__main__':
    intervals = [[0, 0], [0, 0]]
    res = Solution1().merge(intervals)
    print(res)
