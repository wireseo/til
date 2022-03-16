# knowledge: from math import ~
# concepts: power of N
# comment: various approaches, but stay away from the looping solution (maxInt most preferrable)
    # but this method only works as N is prime
# runtime: X, not mine
# memory usage: X, not mine

from math import log10

class Solution:
    # convert the number to base 3 (not available out of the box in python)
    
    # or check if largest 3 power int % 3 == 0
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
        # maxPowerOfThree = pow(3, (log(0x7fffffff) / log(3)) where 0x7fffffff is hexadecimal max pos value for 32-bit signed binary integer

    # or n is a power of three if and only if i = logbn/logb3 is an integer (but may be subject to precision errors)
    # n > 0 because log10 only accepts positive numbers and else it causes math domain error
    def isPowerOfThree(self, n: int) -> bool:
        return (log10(n) / log10(3)) % 1 == 0 if n > 0 else False