# knowledge: X
# concepts: reduce
# comment: use lambda for shorter solution; for time O(1)
# runtime: X, not mine
# memory usage: X, not mine

class Solution:   
    def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")