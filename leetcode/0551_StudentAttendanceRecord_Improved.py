# knowledge: X
# concepts: X
# comment: how did I not think of this solution :0 use count to find consecutive Ls!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') == 0
