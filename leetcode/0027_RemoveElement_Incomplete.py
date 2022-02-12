# knowledge: X
# concepts: two-pointer method
# comment: need to set variable initial status better, remove unnecessary variables
    # have one single purpose for every variable, no need to swap; just copy
# runtime: 43 ms, faster than 51.58% of Python3 online submissions
# memory usage: 13.8 MB, less than 92.42% of Python3 online submissions

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        x = len(nums)
        
        while i < x:
            if nums[i] == val:
                nums[i] = nums[x - 1]
                x -= 1
            else:
                i += 1
        
        return x
        
        # old attempt:
            # i = 0
            # x = len(nums) - 1
            # removedCount = 0
            
            # if x is 0 and nums[x] == val:
            #     return 0
            
            # while i < x:
            #     while nums[x] is val:
            #         removedCount += 1
            #         if x is 0:
            #             return 0
            #         else:
            #             x -= 1
            #     if nums[i] is val:
            #         nums[i] = nums[x]
            #         nums[x] = val
            #         removedCount += 1
            #     i += 1
            # return len(nums) - removedCount
