# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
    
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        before = dummy

        for i in range(left-1):
            before = before.next #node before new start
        
        end = before
        for i in range(right-left+1):
            end = end.next #last node to rev
        
        start = before.next
        after = end.next
        end.next = None
        before.next = None

        before.next = self.reverse(start)
        #after reversing, the previous head of the sublist would be the tail
        start.next = after

        return dummy.next

        
        