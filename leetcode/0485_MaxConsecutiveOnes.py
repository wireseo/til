# knowledge: X
# concepts: max count
# comment: easy question
# runtime: 360 ms, faster than 90.44% of Python3 online submissions
# memory usage: 14.4 MB, less than 9.23% of Python3 online submissions

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        curCount = 0
        
        for num in nums:
            if num == 1:
                curCount += 1
                if curCount > maxCount:
                    maxCount = curCount
            else:
                curCount = 0
        
        return maxCount
