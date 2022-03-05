# knowledge: X
# concepts: Binary tree traversal
# comment: Easy problem
# runtime: 32 ms, faster than 86.10% of Python3 online submissions
# memory usage: 13.8 MB, less than 79.63% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorderList = []
        
        def recurse(root):
            if root:
                recurse(root.left)
                recurse(root.right)
                postorderList.append(root.val)
        
        recurse(root)
        
        return postorderList