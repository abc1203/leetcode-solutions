/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

bool hasCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL) return false;
    struct ListNode *curr = head;
    
    while(curr) {
        if(curr->val == -1000000) return true;
        curr->val = -1000000;
        curr = curr->next;
    }
    return false;
}
