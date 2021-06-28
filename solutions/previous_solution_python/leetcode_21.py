""" Leetcode 21 - Merge Two Soorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

1. Time: O(m+n) Memory: O(1) (m, n are length of l1 and l2)

"""

from common import ListNode


class Solution1:
    """ 1. MINE | Iterative """

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = head_copy = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 is not None else l2
        return head_copy.next


if __name__ == "__main__":
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    l1_head = ListNode.from_list(l1)
    l2_head = ListNode.from_list(l2)
    res_head = Solution1().merge_two_lists(l1_head, l2_head)
    while res_head is not None:
        print(res_head.val)
        res_head = res_head.next
