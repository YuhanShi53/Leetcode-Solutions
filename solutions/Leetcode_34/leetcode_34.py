from typing import List


class Solution1:
    def search_range(self, nums, target):
        def search(target_2):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target_2:
                    right = mid
                else:
                    left = mid + 1
            return left
        starting = search(target)
        return [starting, search(target+1)-1] if target in nums[starting:starting+1] else [-1, -1]


class Solution2:
    def search_range(self, nums, target):
        def divide_and_search(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]
            if nums[left] <= target <= nums[right]:
                mid = left + (right - left) // 2
                l, r = divide_and_search(
                    left, mid), divide_and_search(mid+1, right)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]
        if len(nums) == 0:
            return [-1, -1]
        return divide_and_search(0, len(nums)-1)


class SolutionMINE:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        # Find starting position
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        starting = left
        # Find ending position
        left, right = starting, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 + 1
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [starting, right]


if __name__ == '__main__':
    nums = [1]
    target = 1
    ans = Solution1().search_range(nums, target)
    print(ans)
