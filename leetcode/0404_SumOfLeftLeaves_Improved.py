# knowledge: X
# concepts: binary tree search
# comment: try solving it without helper method next time, single in-place recursion
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(self, root, isLeft=False):
    if not root: return 0
    if not (root.left or root.right): return root.val * isLeft # multiplying by boolean works!
    return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)