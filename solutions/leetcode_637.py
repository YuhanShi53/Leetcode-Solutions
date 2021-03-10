""" Leetcode 637 - Average of Levels in Binary Tree

https://leetcode.com/problems/average-of-levels-in-binary-tree/


"""

from typing import List

from .common import TreeNode


class Solution1:
    """ 1. MINE | BFS | Iteration """

    def average_of_levels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        queue = [root]
        averages = []
        while queue:
            averages.append(sum([node.val for node in queue])/len(queue))
            queue = [kid for node in queue
                     for kid in (node.left, node.right) if kid]
        return averages


if __name__ == '__main__':
    tree_in_list = [3, 9, 20, 15, None, None, 7]
    root = TreeNode.from_list(tree_in_list)
    res = Solution1().average_of_levels(root)
    print(res)
