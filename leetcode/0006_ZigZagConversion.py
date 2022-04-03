# knowledge: 2D array in python = [[_ for col in range()] for row in range()]
# concepts: X
# comment: although it works, it's extremely inefficient; perhaps can reduce the number of for loops
    # row / column order is very confusing
# runtime: 1014 ms, faster than 6% of Python3 online submissions
# memory usage: 17.8 MB, less than 5.17% of Python3 online submissions

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        
        zigzag = [[0 for x in range(len(s)//2 + 1)] for y in range(numRows)] 
        i,j = -1,0
        goingDown = True
        output = []
        
        for char in s:
            if goingDown:
                i += 1
                if i == numRows - 1:
                    goingDown = False
            else:
                i -= 1
                j += 1
                if i == 0:
                    goingDown = True
                    
            zigzag[i][j] = char
        
        for row in range(len(zigzag)):
            for col in range(len(zigzag[row])):
                if zigzag[row][col] != 0:
                    output.append(zigzag[row][col])
            
        return ''.join(output)