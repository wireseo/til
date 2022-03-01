# knowledge: X
# concepts: recursive tree traversal
# comment: try to put base case in recursive method rather than original method
    # better naming than "recurse", try to cut early (line 23) if possible
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def isSymmetric(self, root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            outPair = isMirror(left.left, right.right)
            inPiar = isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False

    return isMirror(root.left, root.right)
