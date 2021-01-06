""" Leetcode 82 - Remove Duplicates From Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

1. Time: O(n) Memory: O(1) (n is length of linked list.)

"""

from common import ListNode


class Solution1:
    """ 1. MINE | Iterative """

    def delete_duplicates(self, head: ListNode) -> ListNode:
        node = node_copy = ListNode(0)
        while head is not None:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
            else:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return node_copy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4, 5, 6, 6]
    head = ListNode.from_list(nums)
    res = Solution1().delete_duplicates(head)
    while res is not None:
        print(res.val)
        res = res.next
