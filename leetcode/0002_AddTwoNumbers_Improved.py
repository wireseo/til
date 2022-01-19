# knowledge: multiple functions in one class requires 'self.'
# concepts: //, %
# comment: shorter code, better naming
# runtime: 64 ms, faster than 92.06% of Python3 online submissions
# memory usage: 14.4 MB, less than 11.65% of Python3 online submissions


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def recursiveAdd(self, l1, l2, nextDigit):
        curDigit = l1.val + l2.val + nextDigit
        nextDigit = curDigit // 10
        curDigit = curDigit % 10
        
        if l2.next is None and l1.next is None:
            if nextDigit == 1:   
                return ListNode(curDigit, ListNode(1))
            else: 
                return ListNode(curDigit)
        elif l2.next is None and l1.next is not None: 
            l2.next = ListNode(0)
        elif l2.next is not None and l1.next is None:
            l1.next = ListNode(0)
            
        return ListNode(curDigit, self.recursiveAdd(l1.next, l2.next, nextDigit))
    
    def addTwoNumbers(self, l1, l2):        
        return self.recursiveAdd(l1, l2, 0)
           