# knowledge: X
# concepts: ranges & intervals
# comment: remove end variable
# runtime: 32 ms, faster than 85.39% of Python3 online submissions
# memory usage: 13.9 MB, less than 27.55% of Python3 online submissions

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        x = 0
        
        while x < len(nums):
            start = nums[x]
            while x < len(nums) - 1 and nums[x+1] == nums[x] + 1:
                x += 1
                
            if start == nums[x]:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + '->' + str(nums[x]))
            
            x += 1
            
        return ranges

    # collect ranges first with tuple, then format them
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,

        return ['->'.join(map(str, r)) for r in ranges]