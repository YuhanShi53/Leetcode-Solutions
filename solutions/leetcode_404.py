""" Leetcode 404 - Sum of Left Leaves

https://leetcode.com/problems/sum-of-left-leaves/

1. MINE BFS: Time: O(n) Space: O(n) (n is num of nodes)

"""

from common import TreeNode


class Solution1:
    """ 1. MINE BFS """

    def sum_of_left_leaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            node = queue.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return res


if __name__ == '__main__':
    tree_nodes = [1, 2, 3, 4, 5]
    root = TreeNode.from_list(tree_nodes)
    res = Solution1().sum_of_left_leaves(root)
    print(res)
