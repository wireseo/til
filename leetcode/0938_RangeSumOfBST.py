# knowledge: X
# concepts: BST
# comment: easy question
# source: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
# runtime: 248 ms, faster than 81.06% of Python3 online submissions
# memory usage: 23 MB, less than 91.65% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.rangeSum = 0
        def recurse(node):
            if node:
                if node.val <= high and node.val >= low:
                    self.rangeSum += node.val
                recurse(node.left)
                recurse(node.right)
            
        recurse(root)
        return self.rangeSum