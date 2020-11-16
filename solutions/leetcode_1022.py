""" Leetcode 1022 - Sum of Root To Leaf Binary Numbers

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

1. MINE BFS: Time: O(n) Space: O(k) (n is num_nodes, k is num_levels)

"""

from collections import deque
from common import TreeNode


class Solution1:
    """ 1. MINE BFS """

    def sum_root_to_leaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        summation = 0
        queue = deque([root])

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.pop()
                if not node.left and not node.right:
                    summation += node.val
                if node.left:
                    node.left.val += node.val * 2
                    queue.appendleft(node.left)
                if node.right:
                    node.right.val += node.val * 2
                    queue.appendleft(node.right)

        return summation


if __name__ == '__main__':
    node_list = [1, 0, 1, 0, 1, 0, 1]
    root = TreeNode.from_list(node_list)
    res = Solution1().sum_root_to_leaf(root)
    print(res)
