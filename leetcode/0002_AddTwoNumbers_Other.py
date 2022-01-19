# non-recursive solution
# comment: easy way to set two variables simultaneously in line 13

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        tmp = head = ListNode(0)
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + carry
            tmp.next = ListNode(s%10)
            carry = s//10
            tmp = tmp.next 
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
        if carry > 0:
            tmp.next = ListNode(1)
        return head.next