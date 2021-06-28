#!/usr/bin/env python

""" Leetcode 23 - Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

Burce-Force: Time: 4864ms Memory: 17.6MB
Divide-and-Merge: Time: 124ms(52.99%) Memory: 17.3MB(93.66%)

"""

from typing import List

from utils import ListNode


class Solution1:
    """Bruce-Froce """

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        temp = lists[0]
        for i in range(1, len(lists)):
            temp = self.merge_two_list(temp, lists[i])
        return temp

    def merge_two_list(self, a: ListNode, b: ListNode):
        temp_head = ListNode()
        pointer = temp_head
        while a is not None and b is not None:
            if a.val <= b.val:
                temp_head.next = a
                a = a.next
            else:
                temp_head.next = b
                b = b.next
            temp_head = temp_head.next
        if a is None:
            temp_head.next = b
        else:
            temp_head.next = a
        return pointer.next


class Solution2:
    """ Divide-and-Merge """

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        length = len(lists)

        while length > 1:
            for i in range(0, length // 2):
                stride = (length + 1) // 2
                lists[i] = self.merge_two_list(lists[i], lists[i+stride])
            length = stride

        return lists[0]

    def merge_two_list(self, a: ListNode, b: ListNode):
        temp_head = ListNode()
        pointer = temp_head
        while a is not None and b is not None:
            if a.val <= b.val:
                temp_head.next = a
                a = a.next
            else:
                temp_head.next = b
                b = b.next
            temp_head = temp_head.next
        if a is None:
            temp_head.next = b
        else:
            temp_head.next = a
        return pointer.next


if __name__ == '__main__':
    temp = [[1, 4, 5], [1, 3, 4], [2, 6]]
    input = [ListNode().reinitialize(x) for x in temp]
    res = Solution2().mergeKLists(input)
    res.nodes
