# knowledge: format(n, "b") --> turns n into binary without 0b in front
# concepts: bit manipulation
# comment: there may be other methods that are faster and more effective
# runtime: 32 ms, faster than 82.22% of Python3 online submissions
# memory usage: 13.8 MB, less than 95.63% of Python3 online submissions

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = format(n, "b")
        prev = temp[0]
        
        for bit in temp[1:]:
            if prev == bit:
                return False
            else:
                prev = bit
        
        return True