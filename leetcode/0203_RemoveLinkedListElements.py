# knowledge: X
# concepts: skipping elements in linked list
# comment: rather than copying the head as cur, create dummy to keep track of head and move along head
# runtime: 64 ms, faster than 97.47% of Python3 online submissions
# memory usage: 17.9 MB, less than 11.71% of Python3 online submissions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        past = dummy
        
        while head:
            if head.val == val:
                past.next = head.next
            else:
                past = head
            head = head.next
        
        return dummy.next
    