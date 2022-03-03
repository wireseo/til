# knowledge: X
# concepts: recursive Pascal's Triangle
# comment: any row can be constructed using the offset sum of the previous row
# runtime: X, not mine
# memory usage: X, not mine

class Solution: 
    def generate(self, numRows):
            res = [[1]]
            for i in range(1, numRows):
                res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
            return res[:numRows]