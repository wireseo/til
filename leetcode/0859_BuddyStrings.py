# knowledge: X
# concepts: num
# comment: use of generator is key for dif
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): 
            return False
        if A == B and len(set(A)) < len(A):
            return True
        
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        
        return len(dif) == 2 and dif[0] == dif[1][::-1]
        