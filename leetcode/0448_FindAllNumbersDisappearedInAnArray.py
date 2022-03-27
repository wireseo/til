# knowledge: abs()
# concepts: array manipulation
# comment: difficult to solve pythonically;
    # For each number i in nums, mark the number that i points as negative.
    # Then filter the list, get all indexes that point to a positive number since those are not visited.
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
                
        return [i + 1 for i, num in enumerate(nums) if num > 0]