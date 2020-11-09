""" Leetcode 105 - Construct Binary Tree From Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

1. Recursive: Time: O(n) Space: O(n)

"""

from common import TreeNode
from typing import List


class Solution1:
    """ 1. Recursive """

    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        node_ids = {val: i for i, val in enumerate(inorder)}
        preorder_id = 0

        def build_sub_tree(low, high):
            nonlocal preorder_id
            if low > high:
                return None
            node = TreeNode(val=preorder[preorder_id])
            preorder_id += 1
            mid = node_ids[node.val]
            node.left = build_sub_tree(low, mid-1)
            node.right = build_sub_tree(mid+1, high)
            return node

        root = build_sub_tree(0, len(inorder)-1)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = Solution1().build_tree(preorder, inorder)
