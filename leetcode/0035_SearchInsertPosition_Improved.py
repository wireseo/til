# knowledge: X
# concepts: binary search & finding return pattern
# comment: to prevent overflow, set midpoint to l + (r - l) // 2
# runtime: X
# memory usage: X

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            midpoint = start + (end - start) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                end = midpoint
            else:
                start = midpoint + 1
                
        return (start + end) // 2
        