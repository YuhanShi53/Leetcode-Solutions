from typing import Optional

from leetcode.python.tree import TreeNode


class Solution1:
    def max_product(self, root: Optional[TreeNode]) -> int:
        self._total = 0
        self._sub_sum = []
        self._dfs(root)
        ret = 0
        for x in self._sub_sum:
            ret = max(ret, x * (self._total - x))
        return ret % (10**9 + 7)

    def _dfs(self, node):
        if not node:
            return 0
        self._total += node.val
        sub_sum = node.val + self._dfs(node.left) + self._dfs(node.right)
        self._sub_sum.append(sub_sum)
        return sub_sum
