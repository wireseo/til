# knowledge: X
# concepts: highest and second highest
# comment: X
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max2 = maxidx = -1 
        
        for idx, num in enumerate(nums):
            if num > max1:
                max2, max1, maxidx  = max1, num, idx
            elif num > max2:
                max2 = num
        return maxidx if max1 >= 2 * max2 else -1
        