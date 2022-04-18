# knowledge: [] * index to create list
# concepts: dynamic programming
# comment: could also use sliding window
# runtime: X, not mine
# memory usage: X, not mine

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                
        return max(dp)

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: 
                anchor = i
            ans = max(ans, i - anchor + 1)

        return ans