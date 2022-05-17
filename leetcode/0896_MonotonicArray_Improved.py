# knowledge: X
# concepts: one pass
# comment: check first and last element!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[-1] < A[0]: 
            A = A[::-1]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True