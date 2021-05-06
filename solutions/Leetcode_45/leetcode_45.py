from typing import List


class Solution1:
    def jump(self, nums):
        n, start, end, thre, step = len(nums), 0, 0, 0, 0
        while thre < n - 1:
            step += 1
            for i in range(start, end+1):
                thre = max(thre, i + nums[i])
                if thre >= n - 1:
                    return step
            if thre == end:
                break
            start, end = end + 1, thre
        return 0 if n == 1 else -1


class SolutionMINE:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step, i, thre = 1, 0, nums[0]
        while thre < len(nums) - 1:
            temp = 0
            for j in range(i+1, thre+1):
                temp = max(temp, j+nums[j])
            i = thre
            thre = temp
            step += 1
        return step


if __name__ == '__main__':
    nums = [1, 2, 3]
    ans = Solution1().jump(nums)
    print(ans)
