# knowledge: enumerate(), dict get(key[, value]) <- value is optional, to be returned when there is no key
# concepts: utilizing two dicts standard comparison vs sorted() comparison
# comment: easy way to fill up dict with key value pairs in lines 22 & 23
# runtime: X, not mine
# memory usage: X, not mine

class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())