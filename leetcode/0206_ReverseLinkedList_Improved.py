# knowledge: X
# concepts: recursion vs iteration for linked list navigation, using "prev" dummy node
# comment: recursive solution is difficult to understand
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    # iterative solution    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            cur.next = prev
            prev = cur
            cur = cur.next

        return prev

    # recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node

    # recursive solution with helper
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev=None):
            if not node:
                return prev
            n = node.next
            node.next = prev

            return reverse(n, node)

        return reverse(head)

        