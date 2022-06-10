# knowledge: X
# concepts: linked list
# comment: fast node doesn't always 'skip' nodes; fast traverses first then slow catches up
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head