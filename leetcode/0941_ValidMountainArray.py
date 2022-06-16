# knowledge: X
# concepts: X
# comment: climb mountain from both sides to match index
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j = 0, len(A) - 1
        
        while i + 1 < len(A) and A[i] < A[i + 1]: 
            i += 1
            
        while j > 0 and A[j - 1] > A[j]: 
            j -= 1
            
        return 0 < i == j < len(A) - 1