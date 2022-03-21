# knowledge: X
# concepts: number manipulation
# comment: trivial solution; is there a better solution?
# runtime: 98 ms, faster than 5.1% of Python3 online submissions
# memory usage: 13.8 MB, less than 65.27% of Python3 online submissions

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        
        while i**2 < num:
            i += 1
        
        return i**2 == num