class Solution1
{
public:
    TreeNode *sortedListToBST(ListNode *head)
    {
        if (head == nullptr)
            return nullptr;
        return bst(head, nullptr);
    }

private:
    TreeNode *bst(ListNode *head, ListNode *tail)
    {
        if (head == tail)
            return nullptr;
        ListNode *fast = head, *slow = head;
        while (fast != tail && fast->next != tail)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        TreeNode *node = new TreeNode(slow->val);
        node->left = bst(head, slow);
        node->right = bst(slow->next, tail);
        return node;
    }
};