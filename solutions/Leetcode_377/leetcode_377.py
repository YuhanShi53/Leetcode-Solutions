from typing import List


class Solution1:
    def combination_sum_4(self, nums, target):
        combination_count = [1] + [0] * target
        for i in range(len(combination_count)):
            for x in nums:
                if x == i:
                    combination_count[i] += 1
                elif x < i:
                    combination_count[i] += combination_count[i-x]
        return combination_count[-1]


class Solution2:
    def combination_sum_4(self, nums, target):
        combination_count = [1] + [-1] * target

        def helper(temp_target):
            if combination_count[temp_target] != -1:
                return combination_count[temp_target]
            total = 0
            for x in nums:
                if temp_target - x >= 0:
                    total += helper(temp_target-x)
            combination_count[temp_target] = total
            return total
        return helper(target)


class SolutionMINE:
    def combination_sum_4(self, nums: List[int], target: int) -> int:
        combination_count = [0] * target
        num_dict = {x: True for x in nums}
        for i in range(target):
            if num_dict.get(i+1, False):
                combination_count[i] += 1
            for j in range(i):
                if num_dict.get(i-j, False):
                    combination_count[i] += combination_count[j]
        print(combination_count)
        return combination_count[-1]


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    ans = Solution2().combination_sum_4(nums, target)
    print(ans)
