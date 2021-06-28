""" Leetcode 669 - Trim a Binary Search Tree

https://leetcode.com/problems/trim-a-binary-search-tree/

1. Time: O(n)

"""

from .common import TreeNode


class Solution1:
    """ 1. MINE | Recursive """

    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        if low <= root.val <= high:
            root.left = self.trim_bst(root.left, low, high)
            root.right = self.trim_bst(root.right, low, high)
            return root
        if low > root.val:
            return self.trim_bst(root.right, low, high)
        return self.trim_bst(root.left, low, high)


if __name__ == '__main__':
    tree_as_list = [3, 0, 4, None, 2, None, None,
                    None, None, 1, None, None, None, None, None]
    root = TreeNode.from_list(tree_as_list)
    low = 1
    high = 3
    res_root = Solution1().trim_bst(root, low, high)
    pass
