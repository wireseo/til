# knowledge: X
# concepts: reversing integers
# comment: find more effective way
# runtime: 38 ms, faster than 72.76% of Python3 online submissions
# memory usage: 13.9 MB, less than 67.93% of Python3 online submissions

class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        isNeg = False
        
        if x < 0:
            x = -x
            isNeg = True
        
        while x:
            digit = x % 10
            x = x // 10
            num = digit + num * 10
            if num > (2 ** 31 - 1):
                return 0
            
        return num if not isNeg else -num