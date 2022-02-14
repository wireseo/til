# knowledge: X
# concepts: sum of subarray pattern
# comment: If the sum of a subarray is positive, it has possible to make the next value bigger, 
    # so we keep do it until it turn to negative.
    # If the sum is negative, it has no use to the next element, so we break.
    # TODO need to figure out divide and conquer method
# runtime: 1279 ms, faster than 20.06% of Python3 online submissions
# memory usage: 28 MB, less than 70.69% of Python3 online submissions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
        