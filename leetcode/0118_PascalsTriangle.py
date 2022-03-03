# knowledge: X
# concepts: recursive Pascal's Triangle
# comment: slow solution
# runtime: 55 ms, faster than 21.52% of Python3 submissions
# memory usage: 14 MB, less than 56.85% of Python3 submissions

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # from row 3, index 1 is sum of index 0 and 1 in row 2
        if numRows == 1:
            return [[1]]
        else:
            pascalList = [[1], [1,1]]
            curRow = 2
            while curRow < numRows:
                idx = 0
                lst = []
                while idx <= curRow:
                    if idx == 0 or idx == curRow:
                        lst.append(1)
                    else:
                        lst.append(pascalList[curRow-1][idx-1] + pascalList[curRow-1][idx])
                    idx += 1
                pascalList.append(lst)
                curRow += 1
                
            return pascalList