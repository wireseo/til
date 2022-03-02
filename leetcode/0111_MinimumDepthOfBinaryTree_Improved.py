# knowledge: map(), numerical or in python will return the first one unless the first one is zero
# concepts: recursive tree counting
# comment: can have multiple iterators in map()
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(self, root):
    if not root: 
        return 0

    d = list(map(self.minDepth, (root.left, root.right))) #[1,2]

    return 1 + (min(d) or max(d))