# knowledge: list = [_] * n to initialize list with n items of _
# concepts: X
# comment: treat row as a string, not a list; we are going to read it horizontally anyway;
    # also just add string with += and reverse the step sign
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows 
        index, step = 0, 1

        for char in s:
            L[index] += char
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)