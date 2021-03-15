""" Leetcode 1721 - Swapping Nodes in a Linked List

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

1. Time: O(n) Memory: O(1)
2. Time: O(n) Memery: O(1)

"""

from .common import ListNode


class Solution1:
    """ 1. MINE | Straight Forward """

    def swap_nodes(self, head: ListNode, k: int) -> ListNode:
        forenode = backnode = head_cp = head
        length = 1
        while head_cp:
            if length == k:
                forenode = head_cp
            head_cp = head_cp.next
            length += 1
        backnode_idx = length - k - 1
        for i in range(backnode_idx):
            backnode = backnode.next
        forenode.val, backnode.val = backnode.val, forenode.val
        return head


class Solution2:
    """ 2. Two Pointer

    Borrow from: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1013859/Python-Solution-with-Explanation

    """

    def swap_nodes(self, head, k):
        slow, fast = head, head
        for _ in range(k-1):
            fast = fast.next
        forenode = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        forenode.val, slow.val = slow.val, forenode.val
        return head


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 3])
    head = Solution2().swap_nodes(head, 2)
    while head:
        print(head.val)
        head = head.next
