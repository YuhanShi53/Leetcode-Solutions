""" Leetcode 107 - Binary Tree Level Order Traversal II

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

1. self-implement BFS: Time: 44ms(19%) Memory: 14.1MB(50%)
2. BFS: Time: 32ms(83%) Memory: 13.9MB(96%)
"""

from utils import TreeNode
from typing import List

class Solution1:
    """ 1. self-implement: BFS """
    def level_order_bottom(self, root) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        traversal = []

        while queue:
            values = []
            next_level = []
            while queue:
                node = queue.pop()
                values.append(node.val)
                if node.left is not None:
                    next_level.insert(0, node.left)
                if node.right is not None:
                    next_level.insert(0, node.right)
            queue = next_level
            traversal.insert(0, values)
        return traversal

class Solution2:
    """ 2. BFS """
    def level_order_bottom(self, root):
        if root is None:
            return []
        queue = [root]
        res = []

        while queue:
            values = []
            level = []
            while queue:
                node = queue.pop()
                if node is not None:
                    values.append(node.val)
                    level.insert(0, node.left)
                    level.insert(0, node.right)
            queue = level
            if len(values) > 0:
                res.insert(0, values)
        return res

if __name__ == '__main__':
    a = [1,2,3,4,5]
    root = TreeNode.from_list(a)
    res = Solution2().level_order_bottom(root)
    print(res)