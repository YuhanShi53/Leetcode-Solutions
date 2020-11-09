class Solution:
    def find_shortest_sub_array(self, nums):
        head_tail_dict = {}
        frequencies_of_nums = {}
        for i, x in enumerate(nums):
            if frequencies_of_nums.get(x, 0):
                frequencies_of_nums[x] += 1
                head_tail_dict[x][1] = i
            else:
                frequencies_of_nums[x] = 1
                head_tail_dict[x] = [i, i]

        max_frequency = 0
        nums_of_max_frequency = []
        for x in frequencies_of_nums:
            if frequencies_of_nums[x] > max_frequency:
                max_frequency = frequencies_of_nums[x]
                nums_of_max_frequency = [x]
            elif frequencies_of_nums[x] == max_frequency:
                nums_of_max_frequency.append(x)
            
        min_length = 50000
        for x in nums_of_max_frequency:
            length_of_num = head_tail_dict[x][1] - head_tail_dict[x][0]
            if length_of_num < min_length:
                min_length = length_of_num

        return min_length + 1

if __name__ == "__main__":
    nums = [1,2,2,3,1,4,4,4,2]
    res = Solution().find_shortest_sub_array(nums)
    print(res)
        