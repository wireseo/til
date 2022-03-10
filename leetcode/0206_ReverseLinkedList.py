# knowledge: append() & pop()
# concepts: X
# comment: next is an in-built function in python, avoid assigning to it when possible
    # only put val in stack, not the node (because it also gets all the '.next' nodes along with it)
    # better recursive and iterative solution possible
# runtime: 54 ms, faster than 46.15% of Python3 online submissions
# memory usage: 16.1 MB, less than 24.42% of Python3 online submissions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = ListNode()
        cur = reversedHead
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
        
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next

        return reversedHead.next
        