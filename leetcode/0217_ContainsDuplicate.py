# knowledge: set.add()
# concepts: set
# comment: easy problem, great intuitive solution of using sets
# runtime: 511 ms, faster than 70.60% of Python3 online submissions
# memory usage: 26 MB, less than 65.92% of Python3 online submissions

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
                
        return False