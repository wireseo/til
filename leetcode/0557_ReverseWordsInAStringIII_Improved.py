# knowledge: X
# concepts: X
# comment: one liner possible! try to utilize __ for _ in ___ syntax
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])
