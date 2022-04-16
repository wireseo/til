# knowledge: X
# concepts: sliding window
# comment: return early
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max = d = 0
        for i in range(len(nums)-k):
            d += nums[i+k] - nums[i]
            if d > max: 
                max = d
            return (sum(nums[:k])+max)/k
