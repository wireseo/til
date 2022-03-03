# knowledge: X
# concepts: recursive Pascal's Triangle
# comment: any row can be constructed using the offset sum of the previous row
    # for _ in range: takes place of variable name, when you are uninterested in iterator value
# runtime: X, not mine
# memory usage: X, not mine

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row