# knowledge: X
# concepts: linked list
# comment: draw it out, think about the order to swap elements 
    # (e.g. before doing prev.next.next = cur, need to change cur.next!)
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
            
        return dummy.next