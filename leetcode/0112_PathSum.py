# knowledge: X
# concepts: recursive tree sum
# comment: nice optimal solution!
# runtime: 54 ms, faster than 64.53% of Python3 submissions
# memory usage: 15 MB, less than 94.85% of Python3 submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def count(node, targetSum):
            if node:
                targetSum -= node.val
                if not node.left and not node.right:
                    return targetSum == 0
                return count(node.left, targetSum) or count(node.right, targetSum)
            
        return count(root, targetSum) and root
