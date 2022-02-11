# knowledge: range(len())
# concepts: two-pointer method
# comment: don't be afraid to overwrite existing content!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1 # independent pointer
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
                
        return x