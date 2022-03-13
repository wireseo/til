# knowledge: X
# concepts: X
# comment: should be a more intuitive way to find power without looping or recursion
# runtime: 47 ms, faster than 50.76% of Python3 online submissions
# memory usage: 13.8 MB, less than 67.81% of Python3 online submissions


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n != 1 and n % 2 == 1:
            return False
        else:
            x = 0
            while pow(2,x) < n:
                x += 1
            if pow(2,x) == n:
                return True
            else:
                return False