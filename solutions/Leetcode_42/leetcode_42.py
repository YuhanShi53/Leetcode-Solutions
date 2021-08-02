from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        left, right, left_max, right_max = 0, len(height) - 1, 0, 0
        water = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] < left_max:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return water


class SolutionMINE:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = 0
        left = []
        for i in range(1, len(height)):
            if height[i] - height[i-1] < 0:
                left.append(i-1)
            elif height[i] - height[i-1] > 0 and left:
                while left and height[i] >= height[left[-1]]:
                    idx = left.pop()
                trap_height = height[i] if left else height[idx]
                idx = left[-1] if left else idx
                water += trap_height * (i - idx - 1) - sum(height[idx+1:i])
                for j in range(idx+1, i):
                    height[j] = trap_height
        return water
