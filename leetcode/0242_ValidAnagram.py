# knowledge: dictionary iteration
# concepts: anagram
# comment: quick and efficient solution with only two loops!
# runtime: 71 ms, faster than 50.33% of Python3 online submissions
# memory usage: 14.5 MB, less than 41.49% of Python3 online submissions

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        
        for char in t:
            if char not in chars or chars[char] == 0:
                return False
            else:
                chars[char] -= 1
                
        return True