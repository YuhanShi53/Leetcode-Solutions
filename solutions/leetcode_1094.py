""" Leetcode 1094 - Car Pooling

https://leetcode.com/problems/car-pooling/

1. Greedy: Time: O(m) Space: O(n) (n is num stops, m is max(num_stops,
                                                            num_trips))

"""

from collections import defaultdict
from typing import List


class Solution1:
    """ 1. Greedy """

    def car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
        last_stop = 0
        num_people_on_trip = defaultdict(int)
        for num, start, end in trips:
            num_people_on_trip[start] += num
            num_people_on_trip[end] -= num
            last_stop = max(last_stop, end)

        for i in range(last_stop):
            capacity -= num_people_on_trip.get(i, 0)
            if capacity < 0:
                return False
        return True


if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    res = Solution1().car_pooling(trips, capacity)
    print(res)
