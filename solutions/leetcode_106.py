""" Leetcode 106 - Construct Binary Tree From Inorder and Postorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

1. Recursive: Time: O(n) Space: O(n)

"""

from typing import List
from common import TreeNode


class Solution1:
    """ 1. Recursive """

    def build_tree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        root_idx = len(inorder) - 1

        def build_sub_tree(low, high):
            nonlocal root_idx
            if low > high:
                return None
            root = TreeNode(postorder[root_idx])
            root_idx -= 1
            mid = inorder_idx[root.val]
            root.right = build_sub_tree(mid+1, high)
            root.left = build_sub_tree(low, mid-1)
            return root

        root = build_sub_tree(0, len(inorder)-1)
        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution1().build_tree(inorder, postorder)
