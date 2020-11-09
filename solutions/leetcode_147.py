""" Leetcode 147 - Insertion Sort List

https://leetcode.com/problems/insertion-sort-list/

1. SM Linked-List-Insertion-Sort: Time: O(n^2) Space: O(1)
2. Linked-List-Insertion-Sort: Time: O(n^2) Space: O(1)

"""


from common import ListNode


class Solution1:
    """ 1. SM Linked-List-Insertion-Sort"""

    def insertion_sort_list(self, head: ListNode) -> ListNode:
        forehead = ListNode(0)
        forehead.next = head
        head = forehead
        while head is not None and head.next is not None:
            current_node = head.next
            second_head = forehead
            while second_head.next is not current_node:
                if current_node.val < second_head.next.val:
                    head.next = current_node.next
                    current_node.next = second_head.next
                    second_head.next = current_node
                    break
                second_head = second_head.next
            if head.next is current_node:
                head = head.next
        return forehead.next


class Solution2:
    """ 2. Linked-List-Insertion-Sort """

    def insertion_sort_list(self, head):
        forehead = ListNode(0)
        prev = forehead
        while head is not None:
            next_node = head.next

            if prev.val > head.val:
                prev = forehead

            while prev.next is not None and prev.next.val < head.val:
                prev = prev.next

            head.next = prev.next
            prev.next = head
            prev = head
            head = next_node
        return forehead.next


if __name__ == '__main__':
    head = ListNode.from_list([1, 5, 3, 4, 0])
    sorted_head = Solution2().insertion_sort_list(head)
    while sorted_head is not None:
        print(sorted_head.val)
        sorted_head = sorted_head.next
