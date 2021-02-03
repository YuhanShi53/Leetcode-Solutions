""" Leetcode 141 - Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

1. Time: O(n) Memory: O(1) (n is length of linked list)

"""

from .common import ListNode


class Solution1:
    """ 1. MINE | Two-Pointer """

    def has_cycle(self, head: ListNode) -> bool:
        faster = head
        while faster and faster.next:
            faster = faster.next.next
            head = head.next
            if faster is head:
                return True
        return False


if __name__ == '__main__':
    head = ListNode.from_list([3, 2, 0, 4])
    head.next.next.next.next = head.next
    res = Solution1().has_cycle(head)
    print(res)
