from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._range_sum = [0]
        for x in nums:
            self._range_sum.append(self._range_sum[-1] + x)

    def sum_range(self, left: int, right: int):
        return self._range_sum[right+1] - self._range_sum[left]
