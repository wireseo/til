# knowledge: define list with for loop, string.ascii_lowercase
# concepts: unrepeated letter
# comment: more classic solution; count() is a C function 
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = [s.index(l) for l in string.ascii_lowercase if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1