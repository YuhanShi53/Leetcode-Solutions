""" Leetcode 264 - Ugly Number II

https://leetcode.com/problems/ugly-number-ii/

1. self-implement: Time: 8824ms(5%) Memory: 14MB(22%)

"""

class Solution1:
    def nth_ugly_number(self, n: int) -> int:
        nums = [1, 2, 3, 5]
        if n < 4:
            return nums[n - 1]

        idx = 1
        while idx < n - 1:
            news = [nums[idx]*x for x in [5, 3, 2]]
            i = idx
            while i < len(nums) and len(news) > 0:
                if nums[i] == news[-1]:
                    news.pop()
                elif nums[i] > news[-1]:
                    if len(news) == 3 and i == n - 1:
                        return news.pop()
                    else:
                        nums.insert(i, news.pop())
                i += 1
            nums += news[::-1]
            idx += 1

        return nums[n-1]

class Solution2:
    def nth_ugly_number(self, n):
        if n <= 0:
            return None
        if n == 1:
            return 1

        w1, w2, w3 = 2, 3, 5
        i1, i2, i3 = 0, 0, 0
        nums = [1 for i in range(n)]
        for i in range(1, n):
            if nums[i1]*w1 == nums[i-1]:
                i1 += 1
            if nums[i2]*w2 == nums[i-1]:
                i2 += 1
            if nums[i3]*w3 == nums[i-1]:
                i3 += 1

            nums[i] = min(nums[i1]*w1, min(nums[i2]*w2, nums[i3]*w3))
        return nums[n-1]

if __name__ == '__main__':
    n = 1352
    res = Solution2().nth_ugly_number(n)
    print(res)