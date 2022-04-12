# knowledge: X
# concepts: X
# comment: trick question; longer string cannot ever be a subsequence of the other
# runtime: 47 ms, faster than 35.53% of Python3 online submissions
# memory usage: 13.9 MB, less than 62.72% of Python3 online submissions

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        
        return max(len(a), len(b))