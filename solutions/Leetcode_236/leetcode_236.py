from leetcode.python.tree import TreeNode


class SolutionMINE():
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)

    def dfs(self, node, p, q):
        if not node:
            return None
        if node is p or node is q:
            return node
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        if left and right:
            return node
        if left or right:
            return left if left else right
        return None
