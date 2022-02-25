from typing import List


class Solution1:
    def max_turbulence_size(self, arr: List[int]) -> int:
        max_size = 1
        local_size = 1
        prev_diff = arr[0] - arr[1] if len(arr) > 1 else 0
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff * prev_diff < 0:
                local_size += 1
                max_size = max(max_size, local_size)
            else:
                local_size = 2
            prev_diff = diff
        return max_size
