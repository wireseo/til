# knowledge: X
# concepts: X
# comment: easy problem, but couldn't immediately think of optimal solution
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1