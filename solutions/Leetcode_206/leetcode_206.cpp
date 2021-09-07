class Solution1
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *prev = nullptr;
        while (head != nullptr)
        {
            ListNode *nextCopy = head->next;
            head->next = prev;
            prev = head;
            head = nextCopy;
        }
        return prev;
    }
};
