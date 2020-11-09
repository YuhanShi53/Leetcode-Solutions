from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        if not nums:
            return 0

        count_dict = defaultdict(int)
        for x in nums:
            count_dict[x] += 1
            
        res = 0
        for x in count_dict.values():
            y = x - 1
            res += (y + 1) * y // 2
            
        return res

if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    res = Solution().numIdenticalPairs(nums)
    print(res)