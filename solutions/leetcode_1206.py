""" Leetcode 1206 - Maximum Difference Between Node and Ancestor

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

1. MINE-BFS-Queue: Time: O(n) Space: O(n) (n is num_of_nodes)
2. Recursive:: Time: O(n) Space: O(n) (n is num_of_nodes)

"""

from common import TreeNode


class Solution1:
    """ 1. MINE-BFS-Queue """

    def max_ancestor_diff(self, root: TreeNode) -> int:
        min_max_queue = [(root.val, root.val)]
        nodes = [root]
        max_diff = 0

        while nodes:
            min_value, max_value = min_max_queue.pop()
            node = nodes.pop()

            new_min = min(min_value, node.val)
            new_max = max(max_value, node.val)
            max_diff = max(max_diff, new_max-new_min)

            if node.left:
                min_max_queue.insert(0, (new_min, new_max))
                nodes.insert(0, node.left)

            if node.right:
                min_max_queue.insert(0, (new_min, new_max))
                nodes.insert(0, node.right)
        return max_diff


class Solution2:
    """ 2. Recursive """

    def max_ancestor_diff(self, root):

        def helper(root, mx, mn):
            if not root:
                return mx - mn
            return max(
                helper(root.left, max(mx, root.val), min(mn, root.val)),
                helper(root.right, max(mx, root.val), min(mn, root.val))
            )

        return helper(root, root.val, root.val)


if __name__ == '__main__':
    tree_list = [8, 3, 10, 1, 6, None, 14, None, None,
                 4, 7, None, None, 13, None]
    root = TreeNode.from_list(tree_list)
    res = Solution2().max_ancestor_diff(root)
    print(res)
