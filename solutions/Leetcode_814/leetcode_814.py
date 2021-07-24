from leetcode.python.tree import TreeNode


class Solution1:
    def prune_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.prune_tree(root.left)
        root.right = self.prune_tree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root
