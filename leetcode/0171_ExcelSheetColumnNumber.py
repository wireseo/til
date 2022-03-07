# knowledge: ord()
# concepts: to get ascii char letter need to subtract 64
# comment: inefficiency from resetting columnTitle list with every iteration
# runtime: 54 ms, faster than 34.34% of Python3 online submissions
# memory usage: 13.9 MB, faster than 21.54% of Python3 online submissions

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 0
        columnNum = 0
        
        while columnTitle:
            columnNum += (ord(columnTitle[-1]) - 64) * pow(26, base)
            base += 1
            columnTitle = columnTitle[:-1]
            
        return columnNum