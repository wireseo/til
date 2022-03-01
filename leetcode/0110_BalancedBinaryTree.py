# knowledge: X
# concepts: recursive tree counting
# comment: follow the definition, some recursion problems need counts
# runtime: X, not mine
# memory usage: X, not mine

#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            if left == -1:
                return -1
            
            right = check(root.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return check(root) != -1