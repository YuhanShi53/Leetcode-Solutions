""" Leetcode 347 - Top-k Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

1. self-implement Hash+Sort: Time: 104ms(84%) Memory: 18MB(15%)

"""
from collections import defaultdict
from typing import List

class Solution1:
    """ 1. self-implement Hash + Sort """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for x in nums:
            count_dict[x] += 1

        x_with_count = [(x, y) for x, y in count_dict.items()]
        x_with_count.sort(key=lambda x: x[1], reverse=True)
        res = [x_with_count[i][0] for i in range(k)]
        return res

if __name__ == '__main__':
    nums = [1]
    k = 1
    res = Solution1().top_k_frequent(nums, k)
    print(res)