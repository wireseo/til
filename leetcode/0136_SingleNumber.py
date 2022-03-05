# knowledge: dict[key] = value
# concepts: X
# comment: X
# runtime: 193 ms, faster than 52.02% of Python3 online submissions
# memory usage: 16.7 MB, less than 44.32% of Python3 online submissions

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = {}
        finalNum = 0
        
        # store every number in arr + add anything that hasnt appeared and subtract if else
        for num in nums:
            if num in numDict:
                finalNum -= num
            else:
                numDict[num] = 1
                finalNum += num
                
        return finalNum