# knowledge: X
# concepts: counter and list manipulation
# comment: need to know how to optimize problems, do it before solving them
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return max([c[x] + c[x + 1] for x in c if x + 1 in c] or [0])
        