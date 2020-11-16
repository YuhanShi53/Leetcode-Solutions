""" Leetcode 938 - Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/

1. Iterative: Time: O(n) Space: O(h) (n is num_of_nodes, h is height_of_tree)
2. Recursive: Time: O(n) Space: O(h) (n is num_of_nodes, h is height_of_tree)

"""

from collections import deque

from common import TreeNode


class Solution1:
    """ 1. MINE-Iterative """

    def range_sum_bst(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        queue = deque([root])
        sumation = 0
        while queue:
            node = queue.pop()
            if low <= node.val <= high:
                sumation += node.val
            if node.left and node.val > low:
                queue.appendleft(node.left)
            if node.right and node.val < high:
                queue.appendleft(node.right)
        return sumation


class Solution2:
    """ 2. Recursive """

    def range_sum_bst(self, root, low, high):
        if root is None:
            return 0
        if root.val < low:
            return self.range_sum_bst(root.right, low, high)
        if root.val > high:
            return self.range_sum_bst(root.left, low, high)
        return (root.val
                + self.range_sum_bst(root.left, low, high)
                + self.range_sum_bst(root.right, low, high))


if __name__ == '__main__':
    root = TreeNode.from_list([10, 5, 15, 3, 7, None, 18])
    low = 7
    high = 15
    res = Solution2().range_sum_bst(root, low, high)
    print(res)
