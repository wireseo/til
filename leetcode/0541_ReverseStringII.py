# knowledge: range(start, stop, step), reversed()
# concepts: list manipulation
# comment: directly replace with reversed section of a list; try to dissect a problem. shouldn't be this challenging...
    # but nice catch that you need to convert back and forth to string for easier manipulation
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        
        for i in range(0, len(a), 2*k): # start, stop, step
            a[i:i+k] = reversed(a[i:i+k])
            
        return "".join(a)