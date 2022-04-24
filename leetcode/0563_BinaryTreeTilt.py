# knowledge: nonlocal keyword
# concepts: Binary Tree (tilt)
# comment: need to keep separate tabs on tilt and return value; had same block for other similar problems
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt
            if not node: return 0

            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            total_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        valueSum(root)
        return total_tilt