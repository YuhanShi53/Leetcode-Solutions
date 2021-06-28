""" Leetcode 143 - Reorder List

https://leetcode.com/problems/reorder-list/


"""

from common import ListNode


class Solution1:
    """ 1. MINE Recursive """

    def reorder_list(self, head: ListNode) -> None:

        def forward(node):
            nonlocal head
            if node is not None and node.next is not None:
                forward(node.next)

            if head is None:
                return
            elif head is node or head.next is node:
                node.next = None
                head = None
            else:
                node.next = head.next
                head.next = node
                head = node.next

        forward(head)


if __name__ == '__main__':
    nums = []
    head = ListNode.from_list(nums)
    head_copy = head
    Solution1().reorder_list(head)
    while head_copy:
        print(head_copy.val)
        head_copy = head_copy.next
