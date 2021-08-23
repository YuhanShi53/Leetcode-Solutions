from typing import Optional

from leetcode.python.tree import TreeNode


class Solution1:
    def find_target(self, root: Optional[TreeNode], k: int) -> bool:
        map = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                target = k - node.val
                if map.get(target, False):
                    return True
                map[node.val] = True
                stack.append(node.left)
                stack.append(node.right)
        return False


class Solution2:
    _root = None

    def find_target(self, root, k):
        if not Solution2._root:
            Solution2._root = root
        if not root:
            return False
        return self._dfs(root, k-root.val) or self.find_target(root.left, k) or self.find_target(root.right, k)

    def _dfs(self, node, k):
        root = Solution2._root
        while root:
            if root.val == k and root != node:
                return True
            if root.val > k:
                root = root.left
            else:
                root = root.right
        return False
