# knowledge: X
# concepts: X
# comment: create list of valid chars then check if equal to its reverse
# runtime: X, not mine
# memory usage: X, not mine

class Solution(object):
    def isPalindrome(self, s):
        chk = [ch.lower() for ch in s if ch.isalnum()]
        return chk == chk[::-1]