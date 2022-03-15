# knowledge: reduce()
# concepts: arrays, bit manipulation, mathematics, set
# comment: sum of 0...n minus sum of given numbers = missing number
    # XOR-ing given numbers and 0...n also works, lots of different solutions
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    # Sum of 0..n minus sum of given numbers
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

    # XOR-ing given numbers and 0..n
    def missingNumber(self, nums):
        return reduce(operator.xor, nums + range(len(nums)+1))

    # XOR-ing with O(1) space
    def missingNumber(self, nums):
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
    
    # Set/Array difference
    def missingNumber(self, nums):
        return (set(range(len(nums)+1)) - set(nums)).pop()