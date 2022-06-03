# knowledge: all(generator)
# concepts: sliding window
# comment: need to familiarize self with sliding window
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p) 
        res, pLen, sLen = [], len(p), len(s)
        
        if pLen > sLen: return []
        
        for i in range(pLen-1):
            if s[i] in counter: 
                counter[s[i]] -= 1

        for i in range(pLen-1, sLen):
            j = i - pLen

            if j >= 0 and s[j] in counter:
                counter[s[j]] += 1

            if s[i] in counter:
                counter[s[i]] -= 1

            if all(v == 0 for v in counter.values()): 
                res.append(j+1)

        return res