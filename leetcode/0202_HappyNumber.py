# knowledge: set(), generator expressions (line 12) 
# concepts: breaking out infinite loops
# comment: remember to use sets! also generator expressions conserve memory
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in mem:
                return False
            mem.add(n)
            
        return True