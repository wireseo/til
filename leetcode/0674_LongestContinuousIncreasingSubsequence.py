# knowledge: X
# concepts: X
# comment: maybe there is a more condensed way; also read question carefully, it could have more than one increasing subsequence
# runtime: 74 ms, faster than 93.13% of Python3 online submissions
# memory usage: 15.3 MB, less than 50.84% of Python3 online submissions

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        prev = -1
        
        for num in nums:
            if prev < num:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
            prev = num
            
        return max(maxCount, count)