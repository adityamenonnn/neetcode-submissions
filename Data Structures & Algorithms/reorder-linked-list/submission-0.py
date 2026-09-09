# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #finding the halves
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        #the first of the second half will now be slow.next
        second = slow.next
        slow.next = None

        #reversing
        curr = second
        prev = None
        while curr : 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #new head i.e the last element in original list will be prev
        #merging
        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2