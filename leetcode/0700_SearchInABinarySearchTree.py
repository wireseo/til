# knowledge: X 
# concepts: BST search
# comment: X
# runtime: 82 ms, faster than 59.95% of Python3 online submissions
# memory usage: 16.5 MB, less than 18.42% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recurse(node):
            if node:
                if node.val == val:
                    return node
                else:
                    return recurse(node.left) or recurse(node.right)
        
        return recurse(root)