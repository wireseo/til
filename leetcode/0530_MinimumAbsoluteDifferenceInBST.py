# knowledge: X
# concepts: BST
# comment: other way that is not dependent on in-order solution? or can do one pass?
# runtime: 68 ms, faster than 64.90% of Python3 online submissions
# memory usage: 16.3 MB, less than 21.72% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDifference = 10001
        self.inorder = []
        
        def recurse(node: TreeNode):
            if node:
                recurse(node.left)
                self.inorder.append(node.val)
                recurse(node.right)

        recurse(root)
        
        for i in range(1, len(self.inorder)):
            minDifference = min(minDifference, abs(self.inorder[i-1] - self.inorder[i]))
    
        return minDifference