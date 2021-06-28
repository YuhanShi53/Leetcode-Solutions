""" Leetcode 2 - Add Two Numbers

https://leetcode.com/problems/add-two-numbers/

1. Time: O(n) Memory: O(1) (n is larger length of l1 and l2)

"""

from common import ListNode


class Solution1:
    """ 1. MINE | Straight-Forward """

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_one = 0
        sum_node = node_copy = ListNode(0)
        while l1 or l2 or add_one:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_node.next = ListNode((l1_val + l2_val + add_one) % 10)
            add_one = (l1_val + l2_val + add_one) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum_node = sum_node.next
        return node_copy.next


if __name__ == '__main__':
    l1 = ListNode.from_list([9, 9, 9])
    l2 = ListNode.from_list([9])
    res = Solution1().add_two_numbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next
