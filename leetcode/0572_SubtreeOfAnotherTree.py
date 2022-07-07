# knowledge: X
# concepts: recursion, BST
# comment: can recurse twice (in helper method and in outer method)
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def recurse(s, t):
            if not (s and t):
                return s is t
            return (s.val == t.val and recurse(s.left, t.left) and recurse(s.right, t.right))
            
        if recurse(s, t): 
            return True
        if not s: 
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        