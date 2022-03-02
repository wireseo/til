# knowledge: X
# concepts: recursive tree counting
# comment: X
# runtime: 623 ms, faster than 74.22% of Python3 online submissions
# memory usage: 54.7 MB, less than 31.03% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def count(node):
            if node:
                if node.left and not node.right:
                    return count(node.left) + 1
                elif not node.left and node.right:
                    return count(node.right) + 1
                else:
                    return min(count(node.left), count(node.right)) + 1
            else:
                return 0
            
        return count(root)