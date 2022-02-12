# knowledge: X
# concepts: overwriting indexes as you loop along
# comment: simple and intuitive method
# runtime: X
# memory usage: X

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: 
            return 0

        res = 0
        for n in nums:
            if n != val:
                nums[res] = n
                res += 1
        return res