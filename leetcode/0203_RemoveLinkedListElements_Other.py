# knowledge: X
# concepts: skipping elements in linked list recursively
# comment: for recursive solutions, just make a good base case and recursive case
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: 
            return None

        head.next = self.removeElements(head.next, val)

        return head.next if head.val == val else head