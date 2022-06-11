# knowledge: X
# concepts: binary tree recursion
# comment: easy binary tree recursion; try to solve it in one line

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if root.left and root.val != root.left.val:
                return False
        
        if root.right and root.val != root.right.val:
                return False
        
        return isUnivalTree(root.left) and isUnivalTree(root.right)
    