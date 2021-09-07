from typing import List


class Solution1:
    def slowest_key(self, releaseTimes: List[int], keysPressed: List[int]) -> str:
        ret_key = keysPressed[0]
        longest_time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > longest_time or duration == longest_time and keysPressed[i] > ret_key:
                longest_time = duration
                ret_key = keysPressed[i]
        return ret_key
