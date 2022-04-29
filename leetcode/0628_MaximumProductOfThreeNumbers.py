# knowledge: X
# concepts: X
# comment: easy, but different way?
# runtime: 274 ms, faster than 80.06% of Python3 online submissions
# memory usage: 15.1 MB, less than 98.20% of Python3 online submissions

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])