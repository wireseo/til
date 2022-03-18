# knowledge: X
# concepts: power of N
# comment: X, look at 326_PowerOfThree for more info on this type of problem
# runtime: 43 ms, faster than 61.4% of Python3 online submissions for Power of Four
# memory usage: 13.9 MB, less than 66.17% of Pythone online submissions

from math import log10

class Solution:
    # convert the number to base 4
    def isPowerOfFour(self, n: int) -> bool:
        return (log10(n) / log10(4)) % 1 == 0 if n > 0 else False