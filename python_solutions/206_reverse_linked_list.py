# Link to problem: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: Last node or empty list
        if (head is None) or (head.next is None):
            return head
        
        # Split up the linked list into two parts:
        # 1: first node
        # 2: rest of the list
        
        # Let's reverse the rest of the list
        rest_list = self.reverseList(head.next);
        
        # Now, let's connect the (reversed) rest of the list
        # to the first node. This means the first node now must
        # become the last node in the list
        head.next.next = head;
        head.next = None;
        
        # Make sure you return the rest of the list!
        return rest_list;
    