# knowledge: X
# concepts: bit/string manipulation
# comment: delete last bit with i << 1
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findComplement(self, num):
        mask = 1 << (len(bin(num)) - 2)
        return (mask - 1) ^ num

    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num