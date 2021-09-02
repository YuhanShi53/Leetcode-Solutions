from typing import List


class Solution1:
    def array_nesting(self, nums):
        visited = [0] * len(nums)
        max_length = 0
        for x in nums:
            length = 0
            while not visited[x]:
                length += 1
                visited[x] = 1
                x = nums[x]
            max_length = max(max_length, length)
        return max_length


class SolutionMINE:
    def array_nesting(self, nums: List[int]) -> int:
        visited = set()
        max_count = 0
        for i, x in enumerate(nums):
            if i not in visited:
                count = 1
                visited.add(i)
                while x != i:
                    x = nums[x]
                    count += 1
                    visited.add(x)
                max_count = max(max_count, count)
        return max_count
