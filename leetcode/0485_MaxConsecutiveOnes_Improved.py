# knowledge: X
# concepts: max count
# comment: make faster by switching conditional placement; but in reality this is slower. Why?
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        curCount = 0
        
        for num in nums:
            if num == 1:
                curCount += 1
            else:
                maxCount = max(maxCount, curCount)
                curCount = 0
        
        return max(maxCount, curCount)
