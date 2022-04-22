# knowledge: height of a tree
# concepts: BST
# comment: need to keep track of the "best" num separate from return value
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def height(p):
            # it's custom to define the height of an empty tree to be -1. This also fixes the off-by-one error I mentioned.
            if not p: 
                return -1       
                            
            left, right = height(p.left), height(p.right)
            
            # the "2 +" accounts for the edge on the left plus the edge on the right. This change is required to account for 
            # the fact that we updated the height of an empty tree to be -1. 
            self.ans = max(self.ans, 2 + left + right)   
            
            return 1 + max(left, right)
            
        height(root)
        return self.ans