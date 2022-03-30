# knowledge: int(x, 2) to create int from bin
# concepts: bit/string manipulation
# comment: utilize if _ else _ for _ format and join string
# runtime: 48 ms, faster than 36.92% of Python3 online submissions
# memory usage: 13.8 MB, less than 56.48% of Python3 online submissions

class Solution:
    def findComplement(self, num: int) -> int:
        binForm = bin(num)[2:]
        return int(''.join('1' if x == '0' else '0' for x in binForm), 2)
