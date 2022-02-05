# knowledge: slice notation in python is lightweight and simple
    # a[start:stop]  items start through stop-1
    # a[start:]      items start through the rest of the array
    # a[:stop]       items from the beginning through stop-1
    # a[:]           a copy of the whole array
    # a[::-1]        reverse the array
# concepts: X
# comment: still don't understand this perfectly
# runtime: X, not mine (but more efficient; 99%)
# memory usage: X, not mine

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if string is same reversed
        if s == s[::-1]: 
            return s
        
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start+size]