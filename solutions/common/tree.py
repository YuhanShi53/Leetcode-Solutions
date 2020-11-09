""" Tree """
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(array: List):
        if not isinstance(array, List):
            raise TypeError('Need a List[value]')
        if array:
            queue = []
            root = TreeNode(array[0])
            queue = [root]
            for i in range(1, len(array), 2):
                node = queue.pop()
                if node is None:
                    continue

                node.left = None if array[i] in [None, 'null'] \
                    else TreeNode(array[i])
                queue.insert(0, node.left)
                node.right = None if array[i + 1] in [None, 'null'] \
                    else TreeNode(array[i + 1])
                queue.insert(0, node.right)
            return root
        return None

    @staticmethod
    def from_inorder_postorder(inorder, postorder):
        """ Build a tree from inorder and postorder list

        Args:
            inorder: list of inorder traversal
            postorder: list of postorder traversal

        Return:
            root of the tree
        """

        if not inorder:
            raise ValueError('Empty inorder list.')
        if not postorder:
            raise ValueError('Empty postorder list.')
        if len(inorder) != len(postorder):
            raise ValueError(
                'Length of inorsder list must be the same as postorder list.')
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        root_idx = len(inorder) - 1

        def build_sub_tree(low, high):
            nonlocal root_idx
            if low > high:
                return None
            root = TreeNode(postorder[root_idx])
            root_idx -= 1
            mid = inorder_idx[root.val]
            root.right = build_sub_tree(mid+1, high)
            root.left = build_sub_tree(low, mid-1)
            return root

        root = build_sub_tree(0, len(inorder)-1)
        return root

    @property
    def width(self):
        """ width of child tree

        Return the width of a child tree of self. The width of a tree is the 
        maximum width among all levels, including the "null" node between the
        leftmost and rightmost non-null node.

        Return:
            int: thesss width of child tree

        """
        level = [(0, self)]
        max_width = 0

        while level:
            current_width = level[-1][0] - level[0][0] + 1
            max_width = max(max_width, current_width)
            level = [
                kid for id, node in level
                for kid in enumerate((node.left, node.right), start=2 * id)
                if kid[1]
            ]
        return max_width

    @staticmethod
    def is_same_tree(root1, root2) -> bool:
        if root1 and root2:
            return root1.val == root2.val and TreeNode.is_same_tree(
                root1.left, root2.left) and TreeNode.is_same_tree(
                    root1.right, root2.right)
        return root1 is root2


if __name__ == '__main__':
    a = [3, 9, 20, 'null', 'null', 15, 7]
    node = TreeNode.from_list(a)
    pass
