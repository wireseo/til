# knowledge: X
# concepts: dictionary
# comment: easy problem, great intuitive solution of using a dictionary
# runtime: 699 ms, faster than 70.55% of Python3 online submissions
# memory usage: 27.3 MB, less than 38.44% of Python3 online submissions

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = {}
        
        for idx, num in enumerate(nums):
            if num in numDict and idx <= k + numDict[num]:
                return True
            numDict[num] = idx
                
        return False