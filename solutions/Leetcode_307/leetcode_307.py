from itertools import accumulate
from typing import List


class Node:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.total = None
        self.start = start
        self.end = end


class NumArray1:
    def __init__(self, nums: List[int]) -> None:
        def create_tree(start, end):
            root = Node(start, end)
            if start == end:
                root.total = nums[start]
                return root
            mid = (start + end) // 2
            root.left = create_tree(start, mid)
            root.right = create_tree(mid+1, end)
            root.total = root.left.total + root.right.total
            return root
        self._nums = nums
        self._n = len(nums)
        self._root = create_tree(0, self._n-1)

    def update(self, index: int, val: int) -> None:
        diff = val - self._nums[index]
        self._nums[index] = val

        def update_util(node):
            if node.start <= index <= node.end:
                node.total += diff
            if node.start == node.end:
                return
            mid = (node.start+node.end) // 2
            if index <= mid:
                update_util(node.left)
            else:
                update_util(node.right)
        update_util(self._root)

    def sumRange(self, left: int, right: int) -> int:

        def sum_range_util(node, start, end):
            if start == node.start and end == node.end:
                return node.total
            mid = (node.start + node.end) // 2
            if right <= mid:
                return sum_range_util(node.left, start, end)
            elif mid < start:
                return sum_range_util(node.right, start, end)
            else:
                return sum_range_util(node.left, start, mid) + sum_range_util(node.right, mid+1, end)

        return sum_range_util(self._root, left, right)


class NumArrayMINE:
    def __init__(self, nums: List[int]) -> None:
        self._sums = list(accumulate(nums))

    def update(self, index: int, val: int) -> None:
        if index == 0:
            diff = val - self._sums[index]
        else:
            diff = val - self._sums[index] + self._sums[index-1]
        for i in range(index, len(self._sums)):
            self._sums[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._sums[right]
        return self._sums[right] - self._sums[left-1]
