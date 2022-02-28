# knowledge: in Python, you can create a nested function instead!
# concepts: recursive tree traversal
# comment: for tree, memorize the helper method
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.helper(root, lst)
        return lst
        
    def helper(self, root: Optional[TreeNode], lst: List[int]):
        if root:
            self.helper(root.left, lst)
            lst.append(root.val)
            self.helper(root.right, lst)