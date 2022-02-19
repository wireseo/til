# knowledge: X
# concepts: fibonacci sequence
# comment: good catch that it was fibonacci, but don't use actual recursion; just use for loop for better memory usage
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a