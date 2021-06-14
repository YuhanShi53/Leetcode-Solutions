import heapq
from typing import List


class Solution1:
    def min_refuel_stops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        distance = idx = 0
        count = -1
        fuels = [-startFuel]
        while distance < target and fuels:
            distance -= heapq.heappop(fuels)
            count += 1
            while idx < len(stations) and distance >= stations[idx][0]:
                heapq.heappush(fuels, -stations[idx][1])
                idx += 1
        return count if distance >= target else -1


class Solution2:
    def min_refuel_stops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i in range(len(stations)):
            for t in range(i+1)[::-1]:
                if dp[t] >= stations[i][0]:
                    dp[t+1] = max(dp[t+1], dp[t] + stations[i][1])
        for i, x in enumerate(dp):
            if x >= target:
                return i
        return -1
