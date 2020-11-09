class Solution:
    def four_sum(self, nums, target):
        
        length_nums = len(nums)
        if length_nums == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        nums.sort()
        res = []

        for i in range(0, length_nums-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length_nums-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                k = j+1
                l = length_nums - 1

                while k != l:

                    if k > j+1 and nums[k] == nums[k-1]:
                        k += 1
                        continue
                    elif l < length_nums-1 and nums[l] == nums[l+1]:
                        l -= 1
                        continue

                    temp_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if temp_sum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                    elif temp_sum < target:
                        k += 1
                    else:
                        l -= 1

        return res

if __name__ == "__main__":

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = Solution().four_sum(nums, target)
    print(res)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:continue
            t = target - nums[i]
            num = nums[i+1:]
            for j in range(len(num)-2):
                if j > 0 and num[j] == num[j-1]:continue
                l = j+1
                r = len(num)-1
                while l < r:
                    val = num[j] + num[l] + num[r]
                    if val == t:
                        res.append([nums[i],num[j],num[l],num[r]])
                        l += 1
                        r -= 1
                        while num[l] == num[l-1] and l < r:
                            l += 1
                        while num[r] == num[r+1] and l < r:
                            r -= 1
                    elif val > t:
                        r -= 1
                    else:
                        l += 1
        return res


class Solution:
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results     