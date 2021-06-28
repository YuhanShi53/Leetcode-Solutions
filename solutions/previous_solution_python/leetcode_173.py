""" Leetcode 173 - Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

1. Time: O(1) Memory: O(H) (H is the height of the tree)
2. Time: O(1) Memory: O(H) (H is the height of the tree)

"""

from common import TreeNode


class BSTIterator:
    """ 1. MINE | Stack | DFS | Inorder Traversal """

    def __init__(self, root: TreeNode):
        self._stack = []
        self._dfs(root)

    def next(self) -> int:
        node = self._stack.pop()
        self._dfs(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self._stack) > 0

    def _dfs(self, node):
        while node is not None:
            self._stack.append(node)
            node = node.left


class BSTIterator2:
    """ 2. Improvement of 1 | Stack | DFS | Inorder Traversal

    Adopted from:
    https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)

    """

    def __init__(self, root):
        self._stack = []
        self._node = root

    def next(self):
        while self._node is not None:
            self._stack.append(self._node)
            self._node = self._node.left
        node = self._stack.pop()
        self._node = node.right
        return node.val

    def hasNext(self):
        return self._node is not None or self._stack


if __name__ == '__main__':
    tree_in_list = [7, 3, 15, None, None, 9, 20]
    root = TreeNode.from_list(tree_in_list)
    iterator = BSTIterator(root)
    print(iterator.next())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
