/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

using namespace std;

class Solution1
{
public:
    ListNode *partition(ListNode *head, int x)
    {
        ListNode head1(0), head2(0);
        ListNode *head1_ptr = &head1, *head2_ptr = &head2;

        while (head)
        {
            if (head->val < x)
            {
                head1_ptr->next = head;
                head1_ptr = head1_ptr->next;
            }
            else
            {
                head2_ptr->next = head;
                head2_ptr = head2_ptr->next;
            }
            head = head->next;
        }
        head2_ptr->next = nullptr;
        head1_ptr->next = head2.next;
        return head1.next;
    }
};