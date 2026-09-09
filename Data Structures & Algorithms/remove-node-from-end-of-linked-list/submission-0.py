class Solution:
    def removeNthFromEnd(self, head, n):
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = reverse(head)

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(n - 1):
            prev = prev.next

        prev.next = prev.next.next        # unlink nth from front

        return reverse(dummy.next)