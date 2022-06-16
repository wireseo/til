# knowledge: use boolean as int 0, 1 (line 16)
# concepts: sliding window
# comment: duplicates so can't use set; keep char dict updated, use while to update start index
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0 # cur window s[i:j] / result window s[I:J]
        
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            
            if not missing: # when window contains all chars of t
                while i < j and need[s[i]] < 0: # while start index is unneeded
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I: # if J hasn't been updated yet or there is new minimum
                    I, J = i, j
                    
        return s[I:J]
