# knowledge: X
# concepts: binary search & finding return pattern
# comment: first immediate pass!
# runtime: 52 ms, faster than 74.65% of Python3 online submissions
# memory usage: 14.9 MB, less than 70.89% of Python3 online submissions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            midpoint = (start + end) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                end = midpoint
            else:
                start = midpoint + 1
                
        return (start + end) // 2
        