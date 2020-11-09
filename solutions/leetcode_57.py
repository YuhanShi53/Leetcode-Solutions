""" Leetcode 57 - Insert Interval

https://leetcode.com/problems/insert-interval/

1. Straight-Forward: Time: O(n) Space: O(n) (n is len_intervals)

"""

from typing import List


class Solution1:
    """ 1. Staight-Forward """

    def insert(self, intervals: List[List[int]], newInterval: List[int]
               ) -> List[List[int]]:

        start, end = newInterval[0], newInterval[1]
        left, right = [], []

        for x in intervals:
            if x[1] < start:
                left.append(x)
            elif x[0] > end:
                right.append(x)
            else:
                start = min(start, x[0])
                end = max(end, x[1])
        return left + [[start, end]] + right


if __name__ == '__main__':
    intervals = [[1, 2], [8, 9]]
    new_intervals = [6, 6]
    res = Solution1().insert(intervals, new_intervals)
    print(res)
