# knowledge: X
# concepts: linked list removal
# comment: weird question; can't actually delete the given node, 
    # need to copy data of next node to cur node and then skip the next node
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next