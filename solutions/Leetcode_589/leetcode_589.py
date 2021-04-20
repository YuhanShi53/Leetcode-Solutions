from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution1:
    def preorder(self, root: Node) -> List[int]:
        if root is None:
            return []
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return traversal
