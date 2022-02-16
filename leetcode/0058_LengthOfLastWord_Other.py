# knowledge: rstrip(): remove trailing characters, split()
# concepts: String manipulation
# comment: learn string manipulation technique
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord(self, s):
        return 0 if not s.split() else len(s.split()[-1])
