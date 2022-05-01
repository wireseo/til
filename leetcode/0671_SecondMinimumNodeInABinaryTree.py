# knowledge: 2 ** 31 for pow
# concepts: binary tree
# comment: need faster method
# runtime: 27 ms, faster than 93.93% of Python3 online submissions
# memory usage: 13.9 MB, less than 66.79% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.smallest = root.val

        def recurse(node):
            if node:
                if node.val > self.smallest:
                    return node.val
                return min(recurse(node.left), recurse(node.right))
            else:
                return 2 ** 31
            
        secondSmallest = recurse(root)
        return secondSmallest if secondSmallest != 2 ** 31 else -1
        