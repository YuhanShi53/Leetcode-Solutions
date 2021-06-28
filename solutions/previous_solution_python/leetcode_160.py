""" Leetcode 160 - Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

1. Time: O(n) Memory: O(1) (n is length of longer list)
2. Time: O(n) Memory: O(1) (n is length of longer list)
3. Time: O(n) Memory: O(1) (n is length of longer list)

"""

from common import ListNode


class Solution1:
    """ 1. MINE | Mark In-place """

    def get_intersection_node(
            self, headA: ListNode, headB: ListNode) -> ListNode:
        head_a_cp, head_b_cp = headA, headB
        while head_a_cp:
            head_a_cp.val *= -1
            head_a_cp = head_a_cp.next
        while head_b_cp and head_b_cp.val > 0:
            head_b_cp = head_b_cp.next
        head_a_cp = headA
        while head_a_cp:
            head_a_cp.val *= -1
            head_a_cp = head_a_cp.next
        return head_b_cp


class Solution2:
    """ 2. Concatenation

    Borrow from: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!

    """

    def get_intersection_node(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


class Solution3:
    """ 3. Length Align

    Borrow from: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49792/Concise-JAVA-solution-O(1)-memory-O(n)-time

    """

    def get_intersection_node(self, headA, headB):
        a, b = headA, headB
        len_a, len_b = 0, 0
        while a:
            a = a.next
            len_a += 1
        while b:
            b = b.next
            len_b += 1
        if len_a > len_b:
            for i in range(len_a - len_b):
                headA = headA.next
        else:
            for i in range(len_b - len_a):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head_a = ListNode.from_list(nums)
    nums = [9, 8, 7]
    head_b = ListNode.from_list(nums)
    intersection_node = head_a
    for i in range(5):
        intersection_node = intersection_node.next
    node_b = head_b
    while node_b.next:
        node_b = node_b.next
    node_b.next = intersection_node
    res_node = Solution3().get_intersection_node(head_a, head_b)
    print(res_node.val)
