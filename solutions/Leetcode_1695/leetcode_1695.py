from typing import List


class Solution1:
    def maximum_unique_subarray(self, nums: List[int]) -> int:
        last_num_index = {}
        maximum = current = 0
        head = 0
        for i, x in enumerate(nums):
            if last_num_index.get(x, -1) >= head:
                current -= sum(nums[head:last_num_index[x]+1])
                head = last_num_index[x] + 1
            current += x
            last_num_index[x] = i
            maximum = max(maximum, current)
        return maximum


class Solution2:
    def maximum_unique_subarray(self, nums):
        unique = set()
        maximum = current = head = 0
        for tail in range(len(nums)):
            while nums[tail] in unique:
                unique.remove(nums[head])
                current -= nums[head]
                head += 1
            unique.add(nums[tail])
            current += nums[tail]
            maximum = max(maximum, current)
        return maximum
