# knowledge: X
# concepts: Floyd's tortoise and hare algorithm (fast and slow pointers)
# comment: use tortoise and hare for "find inner loop" problems
# runtime: 82 ms, faster than 45.90% of Python3 online submissions
# memory usage: 17.5 MB, less than 93.55% of Python3 online submissions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head.next 
        fast = head.next.next

        while slow != fast:
            if not slow or not fast or not fast.next: # reached the end of the linked list
                return False
            slow = slow.next 
            fast = fast.next.next

        return True