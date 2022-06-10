# knowledge: X
# concepts: (binary) search on rotated array
# comment: this is the naive solution; can use binary search to improve time complexity
# runtime: 57 ms, faster than 49.14% of Python3 online submissions
# memory usage: 14.2 MB, less than 22.75% of Python3 online submissions

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        
        return nums[0]