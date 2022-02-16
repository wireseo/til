# knowledge: reversed()
# concepts: String manipulation
# comment: X, easy question
# runtime: 43 ms, faster than 44.86% of Python3 online submissions
# memory usage: 13.9 MB, less than 80.95% of Python3 online submissions

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        for c in reversed(s):
            if c != " ":
                count += 1
            elif count != 0: # when the current blank space is not before the first word
                return count
        return count