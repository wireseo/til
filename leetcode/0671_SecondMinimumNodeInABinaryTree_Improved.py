# knowledge: float('inf') for max val
# concepts: binary tree
# comment: don't always have to create chain of returns in recursive search; just put it in global var
# runtime: X, not mine
# memory usage: X, not mine

def findSecondMinimumValue(self, root):
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

    dfs(root)
    return self.ans if self.ans < float('inf') else -1