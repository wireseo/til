# knowledge: X
# concepts: binary tree
# comment: takes up too much memory -- how to reduce and stabilize?
# runtime: 95 ms, faster than 75.23% of Python3 online submissions
# memory usage: 15.7 MB, less than 20.62% of Python3 online submissions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 and node2:
                return TreeNode(node1.val + node2.val, dfs(node1.left, node2.left), dfs(node1.right, node2.right))
            elif node1:
                return TreeNode(node1.val, dfs(node1.left, None), dfs(node1.right, None))
            elif node2:
                return TreeNode(node2.val, dfs(None, node2.left), dfs(None, node2.right))
            else:
                return None
            
        return dfs(root1, root2)
        