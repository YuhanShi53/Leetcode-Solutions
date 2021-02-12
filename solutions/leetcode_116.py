""" Leetcode 116 - Populating Next Right Pointers in Each Node

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""

from collections import deque


class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution1:
    """ 1. SM """

    def connect(self, root: Node) -> Node:
        if root is None:
            return None
        queue = [root]
        next_start = root.left
        while queue:
            node = queue.pop()
            if node.left is not None:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            if node.next is not None:
                queue.insert(0, node.next)
            if node.next is None and next_start:
                queue.insert(0, next_start)
                next_start = next_start.left
        return root
