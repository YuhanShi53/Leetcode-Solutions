""" Leetcode 103 - Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

1. self-implement Stack: Time: 36ms(56%) Memory: 14MB(28%)

"""

from typing import List
from common import TreeNode


class Solution1:
    """ 1. self-implement Stack """

    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        from_left_to_right = True
        res = []

        while stack:
            level = []
            new_stack = []
            while stack:
                node = stack.pop()
                if from_left_to_right:
                    if node.left:
                        new_stack.append(node.left)
                    if node.right:
                        new_stack.append(node.right)
                else:
                    if node.right:
                        new_stack.append(node.right)
                    if node.left:
                        new_stack.append(node.left)
                level.append(node.val)
            stack = new_stack
            from_left_to_right = not from_left_to_right
            res.append(level)
        return res


if __name__ == '__main__':
    nums = [3, 9, 20, 'null', 'null', 15, 7]
    a_root = TreeNode.from_list(nums)
    result = Solution1().zigzag_level_order(a_root)
    print(result)
