# knowledge: X
# concepts: XOR, bit manipulation
# comment: Xor of any two num gives the difference of bit as 1 and same bit as 0.
    # Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor