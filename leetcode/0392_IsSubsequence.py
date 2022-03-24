# knowledge: X
# concepts: X
# comment: should be faster?
# runtime: 32 ms, faster than 91.26% of Python3 online submissions
# memory usage: 13.8 MB, less than 86.34% of Python3 online submissions

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS, pointerT = 0, 0
        
        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
                
        return pointerS == len(s)