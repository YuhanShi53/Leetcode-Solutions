""" Leetcode 104 - Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

1. Time: 
"""

from common import TreeNode


class Solution1:
    """ 1. MINE """

    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        stack = [root]
        while stack:
            num_node_in_level = len(stack)
            for i in range(num_node_in_level):
                node = stack.pop()
                if node.left is not None:
                    stack.insert(0, node.left)
                if node.right is not None:
                    stack.insert(0, node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    nums = []
    root = TreeNode.from_list(nums)
    max_depth = Solution1().max_depth(root)
    print(max_depth)
