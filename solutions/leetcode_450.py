""" Leetcode 450 - Delete Node in a BST

https://leetcode.com/problems/delete-node-in-a-bst/

1. SM Binary-Search: Time: O(h) Space: (1)

"""

from common import TreeNode


class Solution1:
    """ 1. SM Binary-Search """
    def delete_node(self, root: TreeNode, key: int):
        if not root:
            return None
        node = root
        if node.val == key:
            return self.process_node(node)

        while node:
            if node.left and node.left.val == key:
                new_node = self.process_node(node.left)
                node.left = new_node
                return root
            elif node.right and node.right.val == key:
                new_node = self.process_node(node.right)
                node.right = new_node
                return root
            elif key < node.val:
                node = node.left
            else:
                node = node.right
        return root

    def process_node(self, node: TreeNode):
        if not node.left:
            return node.right
        elif not node.right:
            return node.left

        temp = node.left
        while temp.right:
            temp = temp.right

        temp.right = node.right.left
        node.right.left = node.left
        node = node.right
        return node


if __name__ == '__main__':
    tree_list = [5, 3, 6, 2, 4, None, 7]
    key = 3
    root = TreeNode.from_list(tree_list)
    res_root = Solution1().delete_node(root, key)
