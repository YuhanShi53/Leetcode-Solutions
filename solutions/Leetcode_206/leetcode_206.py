from typing import Optional

from leetcode.python.listnode import ListNode


class Solution1:
    def reverse_list(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        return prev
