# knowledge: Python does not use ! operator, isalnum(), lower()
# concepts: Sliding window
# comment: quick and simple solution
# runtime: 72 ms, faster than 46.37% of Python3 online submissions
# memory usage: 14.6 MB, less than 62.53% of Python3 online submissions

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
                    
        return True