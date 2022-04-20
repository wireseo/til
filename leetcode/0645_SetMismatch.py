# knowledge: sum() to sum record
# concepts: sorting, array, bit manipulation, number manipulation
# comment: so many different approaches!
# runtime: 205 ms, faster than 88.92% of Python3 online submissions (not mine)
# memory usage: 15.8 MB, less than 35.34% of Python3 online submissions (not mine)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), len(nums) * (len(nums) + 1) // 2 - sum(set(nums))]
