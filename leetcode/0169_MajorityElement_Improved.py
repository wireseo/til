# knowledge: range(x, y)
# concepts: X
# comment: more intuitive solution, customized for this problem
# runtime: X
# memory usage: X

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        
        for x in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[x]
            elif major == nums[x]:
                count += 1
            else:
                count -= 1

        return major