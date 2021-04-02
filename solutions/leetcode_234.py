""" Leetcode 234 - Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

1. Time: O(n) Memory: O(1)
2. Time: O(n) Memory: O(1)

"""

from common import ListNode


class Solution1:
    """ 1. Two-Pointers 

    Borrow from: https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

    """

    def is_palindrome(self, head: ListNode) -> bool:
        fast = slow = head
        reverse = None
        while fast and fast.next:
            reverse, reverse.next, slow, fast = slow, reverse, slow.next, fast.next.next
        if fast:
            slow = slow.next
        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next
        return reverse is None


class Solution2:
    """ 2. Restore the original Linked List """

    def is_palindrome(self, head):
        fast = slow = head
        reverse = None
        while fast and fast.next:
            reverse, reverse.next, slow, fast = slow, reverse, slow.next, fast.next.next
        tail = slow.next if fast else slow
        is_palin = True
        while reverse:
            is_palin = is_palin and reverse.val == tail.val
            slow, slow.next, tail, reverse = reverse, slow, tail.next, reverse.next
        return is_palin


if __name__ == '__main__':
    head = ListNode().from_list([1, 2, 3, 3, 1])
    ans = Solution2().is_palindrome(head)
    print(ans)
