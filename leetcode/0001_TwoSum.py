# knowledge: enumerate(), dict = {}
# concepts: dictionary, complements, pair finding
# comment: using python is easier and faster for most problems... 

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if val in dict:
                return [dict[val], idx]
            else:
                dict[complement] = idx
