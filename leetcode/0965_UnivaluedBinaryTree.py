# knowledge: X
# concepts: binary tree recursion
# comment: easy binary tree recursion

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def isEqualToRoot(node):
            if node:
                if node.val == root.val:
                    return isEqualToRoot(node.left) and isEqualToRoot(node.right)
                else:
                    return False
            return True
        
        return isEqualToRoot(root.left) and isEqualToRoot(root.right)