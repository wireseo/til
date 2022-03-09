# knowledge: &, |, <<, >>= etc. bit manipulation
# concepts: bit manipulation
# comment: n & 1 gets last digit of n by bitwise AND with one-digit binary number
    # then add it to ans, and remove last digit of n
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
            
        return ans