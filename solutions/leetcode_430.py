""" Leetcode 430 - Flatten a Multilevel Doubly Linked List

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

1. self-implement Stack: Time: 36ms(73%) Memory: 14.4MB(52%)

"""

from common import DoubleLinkedListNode

class Solution1:
    """ 1. self-immplemnt Stack """
    def flatten(self, head: DoubleLinkedListNode) -> DoubleLinkedListNode:
        if head is None:
            return None
        
        stack = [head]
        head_copy = head
        head = DoubleLinkedListNode(0, 0, 0, 0)

        while stack:
            head.next = stack.pop()
            head.next.prev = head
            head = head.next

            if head.next is not None:
                stack.append(head.next)

            if head.child is not None:
                stack.append(head.child)
                
            head.child = None

        head_copy.prev = None
        return head_copy

if __name__ == '__main__':
    pass