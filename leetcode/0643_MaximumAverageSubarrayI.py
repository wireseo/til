# knowledge: X
# concepts: sliding window
# comment: need to optimize further for speed
# runtime: X, time limit exceeded
# memory usage: X, time limit exceeded

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        index = 0
        maxNum = -10000
        
        while index + k <= len(nums):
            sumNums = 0
            for x in range(index, index + k):
                sumNums += nums[x]
            maxNum = max(maxNum, sumNums / k)
            index += 1
        
        return maxNum