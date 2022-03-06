# knowledge: set()
# concepts: using set to keep track of visited nodes
# comment: nodes are unique objects, thus they are stored as separate items in a set
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        visited = set()
        
        while a:
            visited.add(a)
            a = a.next
        
        while b:
            if b in visited:
                return b
            b = b.next
        
        return None