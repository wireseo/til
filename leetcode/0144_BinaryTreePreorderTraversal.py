# knowledge: X
# concepts: Binary tree traversal
# comment: Easy problem
# runtime: 32 ms, faster than 86.49% of Python3 online submissions
# memory usage: 13.9 MB, less than 79.02% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # O L R
        preorderList = []
        
        def recurse(root):
            if root:
                preorderList.append(root.val)
                recurse(root.left)
                recurse(root.right)
        
        recurse(root)
        
        return preorderList