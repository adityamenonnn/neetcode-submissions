class Solution:
    def removeNthFromEnd(self, head, n):
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        #newhead 
        
        head = reverse(head)
        dummy = ListNode(0,head)
        curr = dummy
        for i in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
    
        
        return reverse(dummy.next)
            


