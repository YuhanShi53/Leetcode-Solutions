from typing import List

from leetcode.python.tree import TreeNode


class Solution1:
    def path_sum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        def dfs(node, path, path_sum):
            path_sum += node.val
            current_path = path + [node.val]
            if not node.left and not node.right and path_sum == targetSum:
                ret.append(current_path)
                return
            if node.left:
                dfs(node.left, current_path, path_sum)
            if node.right:
                dfs(node.right, current_path, path_sum)

        dfs(root, [], 0)
        return ret


class Solution2:
    def path_sum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        stack = [(root, root.val, [root.val])]
        while stack:
            node, current_sum, path = stack.pop()
            if node.left:
                stack.append((node.left, current_sum+node.left.val, path + [node.left.val]))
            if node.right:
                stack.append((node.right, current_sum+node.right.val, path + [node.right.val]))
            if not node.left and not node.right and current_sum == targetSum:
                paths.append(path)
        return paths


class Solution3:
    def path_sum(self, root, targetSum):
        if not root:
            return []
        paths = []
        queue = [(root, root.val, [root.val])]
        while queue:
            node, current_sum, path = queue.pop(0)
            if node.left:
                queue.append((node.left, current_sum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, current_sum + node.right.val, path + [node.right.val]))
            if not node.left and not node.right and current_sum == targetSum:
                paths.append(path)
        return paths
