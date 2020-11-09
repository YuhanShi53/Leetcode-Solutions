# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge_two_lists(self, l1, l2):
        before_head = ListNode(0)
        head = before_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            
            head = head.next

        if l1 is not None:
            head.next = l1
        else:
            head.next = l2
        
        return before_head.next

def transfer_list_to_linked_list(nums):
    before_head = ListNode(0)
    head = before_head
    for x in nums:
        head.next = ListNode(x)
        head = head.next
    return before_head.next

if __name__ == "__main__":
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    l1_head = transfer_list_to_linked_list(l1)
    l2_head = transfer_list_to_linked_list(l2)
    l1_head = None
    l2_head = None
    res_head = Solution().merge_two_lists(l1_head, l2_head)
    while res_head is not None:
        print(res_head.val)
        res_head = res_head.next
        