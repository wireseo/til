# knowledge: multiple functions in one class requires 'self.'
# concepts: recursive Python, better if-else sections
# comment: took an hour. should be quicker... time-efficient but not memory-efficient
    # preset next=None, so no need to repeat while creating object
# runtime: 72 ms, faster than 66.88% of Python3 online submissions
# memory usage: 14.4 MB, less than 11.65% of Python3 online submissions


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def recursiveAdd(self, l1, l2, nextDigit):
        digit = l1.val + l2.val + nextDigit
        if digit > 9:
            nextDigit = 1
            digit = digit - 10
        else:
            nextDigit = 0
            
        if l2.next is None and l1.next is None:
            if nextDigit == 1:   
                return ListNode(digit, ListNode(1, None))
            else: 
                return ListNode(digit, None)
        elif l2.next is None and l1.next is not None: 
            l2.next = ListNode(0, None)
        elif l2.next is not None and l1.next is None:
            l1.next = ListNode(0, None)
            
        return ListNode(digit, self.recursiveAdd(l1.next, l2.next, nextDigit))
    
    def addTwoNumbers(self, l1, l2):        
        return self.recursiveAdd(l1, l2, 0)
           