""" Leetcode 662 - Maximum max_width of Binary Tree

https://leetcode.com/problems/maximum-max_width-of-binary-tree/

1. self-implement BFS: Time: 36ms(78%) Memory: 13.9MB(94%)
2. Simplified BFS: Time: 32ms(93%) Memory: 14.1MB(72%)

"""

from common import TreeNode

class Solution1:
    """ 1. self-implement BFS """
    def width_of_binary_tree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level = [root]
        ids = [0]
        max_width = 0

        while level:
            new_level = []
            new_ids = []
            max_width = ids[0] - ids[-1] + 1
            max_width = max(max_width, max_width)

            while level:
                node = level.pop()
                node_id = ids.pop()
                if node.left is not None:
                    new_level.insert(0, node.left)
                    new_ids.insert(0, node_id * 2)

                if node.right is not None:
                    new_level.insert(0, node.right)
                    new_ids.insert(0, node_id * 2 + 1)
            level = new_level
            ids = new_ids

        return max_width


class Solution2:
    """ 2. Simplified BFS """
    def width_of_binary_tree(self, root):
        if root is None:
            return 0

        level = [(0, root)]
        max_width = 0

        while level:
            current_width = level[-1][0] - level[0][0] + 1
            max_width = max(max_width, current_width)
            level = [kid
                     for id, node in level
                     for kid in enumerate((node.left, node.right), start=2 * id)
                     if kid[1]]
        return max_width


if __name__ == '__main__':
    root = TreeNode.from_list([1, 3, 2, 5, None, None, 9, 6, None, None, None, None, None, None, 7])
    res = Solution2().width_of_binary_tree(root)
    print(res)
                
        