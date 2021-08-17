from leetcode.python.tree import TreeNode


class Solution1:
    def good_nodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, -1e4-1)]
        while stack:
            node, max_value = stack.pop()
            if node:
                if node.val >= max_value:
                    count += 1
                    max_value = node.val
                stack.extend([(node.left, max_value), (node.right, max_value)])
        return count
