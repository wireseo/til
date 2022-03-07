# knowledge: ord()
# concepts: to get ascii char letter need to subtract 64
# comment: X
# runtime: 32 ms, faster than 92.50% of Python3 online submissions
# memory usage: 13.9 MB, faster than 63.62% of Python3 online submissions

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 0
        columnNum = 0
        
        for letter in reversed(columnTitle):
            columnNum += (ord(letter) - 64) * pow(26, base)
            base += 1
            
        return columnNum