# knowledge: X
# concepts: BFS
# comment: use list comprehension to keep appending to level
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans