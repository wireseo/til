# knowledge: X
# concepts: X
# comment: must be a faster way
# runtime: 1054 ms, faster than 32.95% of Python3 online submissions
# memory usage: 14 MB, less than 9.7% of Python3 online submissions

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        
        while n - rows > 0:
            rows += 1
            n -= rows
            
        return rows