# knowledge: X
# concepts: ranges & intervals
# comment: could probably simplify the code more
# runtime: 32 ms, faster than 85.39% of Python3 online submissions
# memory usage: 13.9 MB, less than 27.55% of Python3 online submissions

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        x = 0
        
        while x < len(nums):
            start, end = nums[x], nums[x]
            while x < len(nums) - 1 and nums[x+1] == nums[x] + 1:
                x += 1
                end = nums[x]
                
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + '->' + str(nums[x]))
            
            x += 1
            
        return ranges
