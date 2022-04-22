# knowledge: X
# concepts: BST
# comment: nice solution!
# runtime: 54 ms, faster than 66.77% of Python3 online submissions
# memory usage: 16 MB, less than 94.15% of Python3 online submissions

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if node and node.children:
                # only keep track of the depth of one child with max depth
                return max(map(dfs, node.children)) + 1
            else:
                return 1
        
        return dfs(root) if root else 0

    # alternative version without helper method
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #     return 1 + max((self.maxDepth(node) for node in root.children), default=0)