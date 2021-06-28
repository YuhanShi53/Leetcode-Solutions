""" Leetcode 538 - Convert BST to Greater Tree

https://leetcode.com/problems/convert-bst-to-greater-tree/

1. Time: O(n) Memory: O(n) (n is number of node in the tree)

"""

from .common import TreeNode


class Solution1:
    """ 1. MINE | Dynamic Programming | DFS """

    def convert_bst(self, root: TreeNode) -> TreeNode:
        self._aggregate(root, 0)
        return root

    def _aggregate(self, root, pre_sum):
        if root is None:
            return pre_sum
        root.val += self._aggregate(root.right, pre_sum)
        return self._aggregate(root.left, root.val)


if __name__ == '__main__':
    tree_list = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root = TreeNode.from_list(tree_list)
    res_root = Solution1().convert_bst(root)
    pass
