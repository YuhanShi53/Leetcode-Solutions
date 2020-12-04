""" Leetcode 897 - Increasing Order Search Tree

https://leetcode.com/problems/increasing-order-search-tree/

1. Time: O(N) Space: O(N) (N is num of nodes)

"""

from common import TreeNode


class Solution1:
    """ 1. MINE DFS-Recursion """

    def increasing_bst(self, root: TreeNode) -> TreeNode:
        nums = []

        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            nums.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(root)

        root_cp = root = TreeNode(0)
        for x in nums:
            node = TreeNode(x)
            root.right = node
            root = node
        return root_cp.right


if __name__ == '__main__':
    nums = []
    root = TreeNode.from_list(nums)
    res_tree = Solution1().increasing_bst(root)
