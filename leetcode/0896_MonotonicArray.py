# knowledge: X
# concepts: one pass
# comment: how to reduce time?
# runtime: 1664 ms, faster than 16.77% of Python3 online submissions
# memory usage: 28.1 MB, less than 61.40% of Python3 online submissions

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def cmp(a, b):
            return (a > b) - (a < b) 

        store = 0
        for i in range(len(nums) - 1):
            c = cmp(nums[i], nums[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True