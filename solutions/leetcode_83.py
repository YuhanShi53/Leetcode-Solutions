""" Leetcode 83 - Remove Duplicates From Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

from common import ListNode


class Solution1:
    """ 1. MINE | Iterative """

    def delete_duplicate(self, head: ListNode) -> ListNode:
        node = node_copy = ListNode(-200)
        while head is not None:
            if node.val < head.val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return node_copy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4, 5]
    head = ListNode.from_list(nums)
    res = Solution1().delete_duplicates(head)
    while res is not None:
        print(res.val)
        res = res.next
