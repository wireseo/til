# knowledge: maintain max and min
# concepts: arrays, DP
# comment: only swap max and min when there is a negative number & max/min are updated
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        imax, imin = r, r 
    
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            r = max(r, imax)
        
        return r
