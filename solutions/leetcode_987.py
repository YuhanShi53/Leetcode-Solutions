""" Leetcode 987 - Vertical Order Traversal of a Binary Tree

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


"""

from collections import defaultdict
from typing import List

from common import TreeNode


class Solution1:
    """ 1. SM """

    def vertical_travesal(self, root: TreeNode) -> List[List[int]]:
        traversal = defaultdict(dict)
        min_col, max_col, max_depth = 0, 0, 0

        def bfs(node, x, y):
            nonlocal min_col, max_col, max_depth
            if node:
                if traversal[x].get(y, False):
                    traversal[x][y].append(node.val)
                else:
                    traversal[x][y] = [node.val]
                min_col = min(min_col, x)
                max_col = max(max_col, x)
                max_depth = min(max_depth, y)

                bfs(node.left, x-1, y-1)
                bfs(node.right, x+1, y-1)

        bfs(root, 0, 0)
        res = []
        for col in range(min_col, max_col+1):
            if traversal.get(col, False):
                res.append([])
            for row in range(0, max_depth-1, -1):
                if traversal[col].get(row, False):
                    res[-1].extend(sorted(traversal[col][row]))
        return res


if __name__ == '__main__':
    root = TreeNode.from_list([0])
    res = Solution1().vertical_travesal(root)
    print(res)
