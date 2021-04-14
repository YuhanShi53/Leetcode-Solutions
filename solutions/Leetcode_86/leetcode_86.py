from solutions.common import ListNode


class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head_1 = head_1_cp = ListNode(0)
        head_2 = head_2_cp = ListNode(0)
        while head:
            if head.val < x:
                head_1_cp.next = head
                head_1_cp = head_1_cp.next
            else:
                head_2_cp.next = head
                head_2_cp = head_2_cp.next
            head = head.next
        head_2_cp.next = None
        head_1_cp.next = head_2.next
        return head_1.next


class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        while head and head.val < x:
            prev, head = head, head.next
        temp = prev
        while head:
            if head.val < x:
                prev.next = head.next
                head.next = temp.next
                temp.next = head
                temp = temp.next
                head = prev.next
            else:
                prev = head
                head = head.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode.from_list([1, 4, 3, 2, 5, 2])
    ans = Solution1().partition(head, 3)
    while ans:
        print(ans.val)
        ans = ans.next
