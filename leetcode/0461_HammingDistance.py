# knowledge: X
# concepts: binary manipulation
# comment: count number of 1 in XOR of x and y; fast and efficient solution!
# runtime: 41 ms, faster than 58.85% of Python3 online submissions
# memory usage: 13.7 MB, less than 97.54% of Python3 online submissions

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        combined = bin(x ^ y)[2:]
        return combined.count("1")