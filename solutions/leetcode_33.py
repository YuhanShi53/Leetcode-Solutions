# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution_1:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        left_pointer = 0
        right_pointer = len(nums) - 1
        while(left_pointer <= right_pointer):
            if nums[left_pointer] <= target:
                if nums[left_pointer] == target:
                    return left_pointer
                else:
                    left_pointer += 1
            elif nums[right_pointer] >= target:
                if nums[right_pointer] == target:
                    return right_pointer
                else:
                    right_pointer -= 1
            else:
                return -1
        return -1

class Solution_2:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        self.nums = nums
        self.target = target

        return self.__binary_search_between(0, len(nums)-1)
        
    def __binary_search_between(self, left_pointer, right_pointer):
        if left_pointer > right_pointer:
            return -1
        
        mid_pointer = (left_pointer + right_pointer) // 2
        if self.nums[mid_pointer] == self.target:
            return mid_pointer

        if self.__is_sorted_between(left_pointer, mid_pointer):
            if self.nums[left_pointer] <= self.target and self.nums[mid_pointer] >= self.target:
                return self.__binary_search_between(left_pointer, mid_pointer-1)
            return self.__binary_search_between(mid_pointer+1, right_pointer)
        elif self.nums[mid_pointer] <= self.target and self.nums[right_pointer] >= self.target:
            return self.__binary_search_between(mid_pointer+1, right_pointer)
        return self.__binary_search_between(left_pointer, mid_pointer)

    def __is_sorted_between(self, left_pointer, right_pointer):
        if self.nums[left_pointer] >= self.nums[right_pointer]:
            return True
        else:
            return False


if __name__ == "__main__":
    nums = [3,1]
    target = 1
    res = Solution_2().search(nums, target)
    print(res)