# knowledge: >>= etc.
# concepts: bit manipulation
# comment: easy but slow solution -- how to improve?
# runtime: 60 ms, faster than 15.91% of Python3 online submissions
# memory usage: 13.8 MB, less than 67.80% of Python3 online submissions

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        
        return count