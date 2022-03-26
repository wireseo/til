# knowledge: X
# concepts: pure math
# comment: this is an arithmetic sequence, thus is solvable in O(1)
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8 * n)**0.5) // 2)