# knowledge: X
# concepts: recursive tree traversal
# comment: clean code completed in minimum time!
# runtime: 54 ms, faster than 60.35% of Python3 online submissions
# memory usage: 16.3 MB, less than 22.52% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:       
        def recurse(root, maxDepth):
            if root:
                return max(recurse(root.left, maxDepth + 1), recurse(root.right, maxDepth + 1))
            else:
                return maxDepth
            
        return recurse(root, 0)