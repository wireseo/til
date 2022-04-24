# knowledge: list.sort() vs sorted(list) -- sorted returns a new list while sort returns None
# concepts: X
# comment: nice quick solution!
# runtime: 285 ms, faster than 82.51% of Python3 online submissions
# memory usage: 16.8 MB, less than 53.26% of Python3 online submissions

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # pair with closest neighbor (min gets sacrificed to max in pair)        
        return sum(sorted(nums)[::2])