# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def search_range(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        self.probable_position = []
        self.binary_search(nums, target, 0, len(nums)-1)
        if len(self.probable_position) == 0:
            return [-1, -1]
        else:
            return [min(self.probable_position), 
                    max(self.probable_position)]
        
    def binary_search(self, nums, target, left_pointer, right_pointer):
        if left_pointer > right_pointer:
            return
        
        mid_pointer = (left_pointer + right_pointer) // 2
        if nums[mid_pointer] == target:
            self.probable_position.append(mid_pointer)

        if nums[left_pointer] <= target and target <= nums[mid_pointer]:
            self.binary_search(nums, target, left_pointer, mid_pointer-1)
        if nums[mid_pointer] <= target and target <= nums[right_pointer]:
            self.binary_search(nums, target, mid_pointer+1, right_pointer)


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 6
    res = Solution().search_range(nums, target)
    print(res)