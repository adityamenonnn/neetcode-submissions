# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #dummy is to make sure that im not putting it into an empty list
        dummy = ListNode()
        tail = dummy
        
        #given in the q that more are nodes 
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next #updating the pointer on list 1
            else:
                tail.next = l2
                l2 = l2.next
            #always have to change the tail from the previous last element to the actual last element
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next 