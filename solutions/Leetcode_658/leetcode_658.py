from typing import List


class Solution1:
    def find_closest_elements(self, arr, k, x):
        left = 0
        right = len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]


class Solution2:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_elements = []
        for y in arr:
            if len(closest_elements) < k:
                closest_elements.append(y)
            elif abs(y - x) < abs(closest_elements[0] - x):
                closest_elements.remove(closest_elements[0])
                closest_elements.append(y)
        return closest_elements
