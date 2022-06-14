# knowledge: X
# concepts: X
# comment: possible min is min + k, possible max is max - k, think simple!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums) - k
        mini = min(nums) + k
        return max(0, maxi-mini)