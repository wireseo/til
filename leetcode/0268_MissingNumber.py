# knowledge: X
# concepts: arrays
# comment: good solution, but could you do it with bit manipulation?
# runtime: 148 ms, faster than 79.76% of Python3 online submissions
# memory usage: 15.3 MB, less than 51.83% of Python3 online submissions

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for idx, num in enumerate(sorted(nums)):
            if idx != num:
                return idx
        return len(nums) # when all subsequent numbers were present, the missing number is max + 1