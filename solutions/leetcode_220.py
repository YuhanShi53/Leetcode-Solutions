""" Leetcode 220 - Contains Duplicate III

https://leetcode.com/problems/contains-duplicate-iii/

1. Bucket-Sort: Time: O(n) Space: O(k) (n is len(nums))

"""


from typing import List


class Solution1:
    """ 1. Bucket-Sort """

    def contains_nearby_almost_duplicate(
            self, nums: List[int], k: int, t: int) -> bool:
        INT_MIN = -2**31 + 1
        if k < 1 or t < 0:
            return False
        bucket = {}
        for i, x in enumerate(nums):
            remapped_x = (x - INT_MIN) // (t + 1)
            if (remapped_x in bucket.keys()
                    or remapped_x - 1 in bucket.keys()
                    and x - bucket[remapped_x-1] <= t
                    or remapped_x + 1 in bucket.keys()
                    and bucket[remapped_x+1] - x <= t):
                return True
            # remove out-of-range element
            if len(bucket) >= k:
                bucket.pop((nums[i-k] - INT_MIN)//(t+1), 0)
            bucket[remapped_x] = x
        return False


if __name__ == '__main__':
    nums = [3, 6, 0, 2]
    k = 2
    t = 2
    res = Solution1().contains_nearby_almost_duplicate(nums, k, t)
    print(res)
