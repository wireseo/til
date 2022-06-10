# knowledge: X
# concepts: palindrome
# comment: need to optimize further
# runtime: 253 ms, faster than 44.66% of Python3 online submissions
# memory usage: 14.5 MB, less than 29.85% of Python3 online submissions

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        def checkPalindrome(left, right):
            if left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                checkPalindrome(left-1, right+1)
            
        for i, c in enumerate(s):
            self.count += 1
            checkPalindrome(i-1, i+1)
            if i < len(s) - 1 and c == s[i+1]: 
                checkPalindrome(i, i+1)
                
        return self.count