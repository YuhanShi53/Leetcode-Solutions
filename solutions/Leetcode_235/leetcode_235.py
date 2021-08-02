from leetcode.python.tree import TreeNode


class Solution1:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            return self.lowest_common_ancestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowest_common_ancestor(root.right, p, q)
        return root


class Solution2:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root
