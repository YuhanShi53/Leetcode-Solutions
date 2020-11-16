# https://leetcode.com/problems/next-permutation/

class Solution:
    def next_permutation(self, nums):
        if len(nums) == 0:
            return
        elif len(nums) == 1:
            return

        pointer = len(nums) - 2
        while(pointer >= 0):
            if nums[pointer] < nums[pointer + 1]:
                self.__change_number_at_pointer(pointer, nums)
                return
            pointer -= 1
        nums[0::] = nums[-1::-1]

    def __change_number_at_pointer(self, pointer, nums):
        MINEallest_candidate_index = self.__find_MINEallest_candidate_before(
            pointer, nums)
        self.__exchange_numbers_of_indices(
            pointer, MINEallest_candidate_index, nums)
        self.__transpose_sequence_before(pointer, nums)

    def __find_MINEallest_candidate_before(self, pointer, nums):
        for i in range(len(nums)-1, pointer, -1):
            if nums[i] > nums[pointer]:
                return i

    def __exchange_numbers_of_indices(self, index_1, index_2, nums):
        nums[index_1], nums[index_2] = nums[index_2], nums[index_1]

    def __transpose_sequence_before(self, pointer, nums):
        nums[pointer+1::] = nums[len(nums)-1:pointer:-1]


if __name__ == "__main__":
    nums = [7, 6, 5, 4]
    Solution().next_permutation(nums)
    print(nums)
