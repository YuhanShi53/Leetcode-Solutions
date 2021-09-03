from functools import lru_cache
from typing import List, Optional

from leetcode.python.tree import TreeNode


class Solution1:
    def generate_trees(self, n: int) -> List[Optional[TreeNode]]:
        return self._generate_trees_in_range(1, n)

    @lru_cache
    def _generate_trees_in_range(self, m, n):
        if m > n:
            return [None]
        trees = []
        for x in range(m, n+1):
            left_trees = self._generate_trees_in_range(m, x-1)
            right_trees = self._generate_trees_in_range(x+1, n)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    node = TreeNode(x)
                    node.left = left_tree
                    node.right = right_tree
                    trees.append(node)
        return trees
