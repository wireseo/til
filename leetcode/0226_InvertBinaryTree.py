# knowledge: X
# concepts: binary tree invert
# comment: easy problem but probably a way to make it a bit more concise
# runtime: 36 ms, faster than 74.40% of Python3 online submissions
# memory usage: 13.8 MB, less than 97.51% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node):
            if node:
                dummy = node.left
                node.left = node.right
                node.right = dummy
                
                recurse(node.left)
                recurse(node.right)
            
        recurse(root)
        return root