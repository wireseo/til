# knowledge: dict.get(key, default val if key doesn't exist), self.mode to use in helper method
# concepts: BST, dictionary
# comment: difficult; can implement a counter and count without messing up recursive flow
# runtime: X, not mine
# memory usage: X, not mine

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.mode = 0
        dictionary = {}
    
        def traverse(node: TreeNode, dictionary: dict):
            if not node: return

            dictionary[node.val] = dictionary.get(node.val, 0) + 1
            self.mode = max(self.mode, dictionary[node.val])

            traverse(node.left, dictionary)
            traverse(node.right, dictionary)

        traverse(root, dictionary)
        
        keys = []
        for key, value in dictionary.items():
            if value == self.mode:
                keys.append(key)

        return keys
