# knowledge: for i in range()
# concepts: attempt to expand from center for palindromic questions
# comment: more innovative thinking & approaches needed
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def longestPalindrome(self, s):
        self.maxLen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s,i,i) # odd case
            self.expandFromCenter(s,i,i + 1) # even case
        return s[self.start : self.start + self.maxLen]


    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxLen < r - l - 1:
            self.maxLen = r - l - 1
            self.start = l + 1