# knowledge: X
# concepts: reversing integers
# comment: but is this really a better version to my solution?
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0