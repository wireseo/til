# knowledge: ''.format() if else
# concepts: X
# comment: don't know why logic got tangled...
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def tree2str(self, t):
        if not t: 
            return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)