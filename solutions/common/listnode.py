""" Linked List Data Structure

Leetcode denote linked list as ListNode, so we follow Leetcode here.
"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reinitialize(self, input=None):
        if input is None:
            return self
        if isinstance(input, list):
            header = ListNode.from_list(input)
        return header

    @staticmethod
    def from_list(nums: List):
        """ Initialize a new Linked List from a list

        Args:
            nums: a list of numbers

        Return:
            the head of the Linked List
        """

        header = ListNode()
        temp = header
        for x in nums:
            temp.next = ListNode(x)
            temp = temp.next
        return header.next

    @property
    def nodes(self):
        temp = self
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def remove_elements(self, val):
        """ Remove nodes from a Linked List which have value val

        Args:
            val: value to remove

        Return:
            head of modified Linked List
        """

        if self is None:
            return None
        head = self
        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return self if self.val != val else self.next


class DoubleLinkedListNode:
    def __init__(self, val=0, next=None, prev=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child
