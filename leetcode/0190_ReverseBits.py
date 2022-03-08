# knowledge: &, |, <<, >>= etc. bit manipulation
# concepts: bit manipulation
# comment: need to study bit manipulation
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
            
        return ans