/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */



struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *lst = NULL;     
    
    while(list1 || list2) {
        struct ListNode *newNode = malloc(sizeof(struct ListNode));
        newNode->next = NULL;
        
        if(!list1) {
            newNode->val = list2->val;
            list2 = list2->next;
        } else if(!list2) {
            newNode->val = list1->val;
            list1 = list1->next;
        } else if(list1->val <= list2->val) {
            newNode->val = list1->val;
            list1 = list1->next;
        } else {
            newNode->val = list2->val;
            list2 = list2->next;
        }
        
        struct ListNode *curr = lst;
        if(curr == NULL) {
            lst = newNode;
        } else {
            while(curr->next) {
                curr = curr->next;
            }
            curr->next = newNode;
        }
    }
    
    return lst;
}
