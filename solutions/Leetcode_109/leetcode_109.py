class Solution1:
    def sorted_listed_to_bst(self, head):
        if head:
            return self.bst(head, None)
        return None

    def bst(self, head, tail):
        if head == tail:
            return None
        fast = slow = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        node = TreeNode(slow.val)
        node.left = self.bst(head, slow)
        node.right = self.bst(slow.next, tail)
        return node
