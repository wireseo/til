# knowledge: X
# concepts: recursive tree traversal
# comment: simplify return statements
# runtime: 54 ms, faster than 39.32% of Python3 submissions
# memory usage: 13.9 MB, less than 81.62% of Python3 submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recurse(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left and right:
                return left.val == right.val and recurse(left.left, right.right) and recurse(left.right, right.left)
            elif not left and not right:
                return True
        
        if root.left and root.right:
            return recurse(root.left, root.right)
        elif not root.left and not root.right: # root is always symmetrical
            return True 
        else:
            return False