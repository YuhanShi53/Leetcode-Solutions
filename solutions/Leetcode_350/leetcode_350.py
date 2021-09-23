from collections import defaultdict
from typing import List

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        num_dict = defaultdict(int)
        for x in nums1:
            num_dict[x] += 1
        for x in nums2:
            if num_dict.get(x, 0):
                intersection.append(x)
                num_dict[x] -= 1
        return intersection
