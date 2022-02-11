# knowledge: X
# concepts: python linked lists, loop while Node, not while Node.next is not None
# comment: no need to while loop end cases, just set it equal to the list that is left over
    # no need for list3 var, no need for new node creation; just reuse existing node
    # make new vars for pointer for existing list
    # naming scheme = dummy?
# runtime: X
# memory usage: X

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = curNode = ListNode()
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                curNode.next = p1
                p1 = p1.next
            else:
                curNode.next = p2
                p2 = p2.next
            curNode = curNode.next

        if p1:
            curNode.next = p1
        elif p2:
            curNode.next = p2
                
        return list3.next