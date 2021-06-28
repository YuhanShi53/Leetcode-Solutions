""" Leetcode 203 - Removoe Linked List Elements

https://leetcode.com/problems/remove-linked-list-elements/

1. self-implement With Dummy Head: Time: 68ms(88%) Memory: 17MB(19%)
2. Without Dummy Head: Time: 72ms(73%) Memory: 17MB(11%)

"""

from common import ListNode


class Solution1:
    """ 1. self-implement With Dummy Head """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        head_prev = ListNode(0, head)
        head = head_prev
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return head_prev.next


class Solution2:
    """ 2. Without Dummy Head """
    def remove_elements(self, head, val):
        if head is None:
            return None
        head_copy = head
        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return head_copy if head_copy.val != val else head_copy.next


if __name__ == '__main__':
    nums = [1, 2, 6, 3, 4, 5, 6]
    head = ListNode().reinitialize(nums)
    val = 6
    new_head = Solution2().remove_elements(head, val)
    new_head.nodes