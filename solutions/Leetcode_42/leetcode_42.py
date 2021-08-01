from typing import List


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
