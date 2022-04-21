# knowledge: X
# concepts: BST, generator
# comment: can get rid of minDifference var, more intuitive function names (dfs)
    # no need for self var? also no need to define var type in helper function
# runtime: 54 ms, faster than 93.69% of Python3 online submissions
# memory usage: 16.3 MB, less than 7.20% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                inorder.append(node.val)
                dfs(node.right)

        dfs(root)
        
        return min(b - a for a,b in zip(inorder, inorder[1:]))