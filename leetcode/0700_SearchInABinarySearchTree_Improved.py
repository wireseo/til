# knowledge: X 
# concepts: BST search
# comment: it's a BST! only search left or right
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root