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
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        // creates a sorted list; 1st elem goes to sorted
        // sorted is the head of the sorted list
        ListNode* sorted = head;
        head = head->next;
        sorted->next = NULL;

        // passes head into sorted for each elem
        while(head != NULL) {
            // put into correct position
            ListNode* curr = sorted;
            ListNode* prev = NULL;
            while(curr != NULL && head->val > curr->val) {
                prev = curr;
                curr = curr->next;
            }

            // need prev -> head -> curr
            ListNode* to_add = head;
            head = head->next;

            if(prev == NULL) {
                to_add->next = curr;
                sorted = to_add;
            } else {
                prev->next = to_add;
                to_add->next = curr;
            }
        }
        return sorted;
    }
};
