# knowledge: n &= n - 1
# concepts: bit manipulation
# comment: n = XXXXXX1000, n - 1 = XXXXXX0111. n & (n - 1) = XXXXXX0000 which removes the last significant 1
# runtime: X, not mine
# memory usage: X, not mine

def hammingWeight(self, n):
    count = 0
    while n:
        n &= n - 1
        count += 1

    return count