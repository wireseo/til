# knowledge: X
# concepts: binary tree search
# comment: read the question carefully -- not left nodes, but left leaves
    # can optimize by setting isLeft=False as default, only setting True for left leaves
# runtime: 47 ms, faster than 52.28% of Python3 online submissions
# memory usage: 14.9 MB, less than 21.33% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recurse(node, isLeft):
            if node:
                if isLeft and not node.left and not node.right: # if it is a left leaf
                    return node.val
                else:
                    return recurse(node.left, True) + recurse(node.right, False)
            else:
                return 0



        return recurse(root, False)