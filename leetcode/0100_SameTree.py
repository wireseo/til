# knowledge: no need to reiterate variable type for nested function
# concepts: recursive tree traversal
# comment: always make base case!
# runtime: 28 ms, faster than 94.69% of Python3 submissions
# memory usage: 13.9 MB, less than 65.05% of Python3 submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(p, q):
            if p and q:
                return recurse(p.left, q.left) and (p.val == q.val) and recurse(p.right, q.right)
            elif p == None and q == None:
                return True
            
        return recurse(p, q)
