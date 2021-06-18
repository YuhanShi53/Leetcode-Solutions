from typing import List


class Solution1:
    def num_subarray_bounded_max(self, nums, left, right):
        prev = 0
        last_invalid = -1
        count = 0
        for i, x in enumerate(nums):
            if x > right:
                prev = 0
                last_invalid = i
            elif left <= x:
                prev = i - last_invalid
            count += prev
        return count


class SolutionMINE:
    def num_subarray_bounded_max(self, nums: List[int], left: int, right: int) -> int:
        nums.append(right+1)
        q = []
        idx = -1
        count = 0
        for i, x in enumerate(nums):
            if left <= x <= right:
                q.append(i-idx)
                idx = i
            elif x > right:
                if q:
                    q.append(i-idx)
                    for d in range(1, len(q)):
                        for y in range(0, len(q)-d):
                            count += q[y] * q[y+d]
                    q.clear()
                idx = i
        return count
