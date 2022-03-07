# knowledge: max(list, key)
# concepts: X
# comment: memorize add to dict logic; there should be a faster way to solve this problem
# runtime: 321 ms, faster than 11.97% of Python3 online submissions
# memory usage: 15.5 MB, less than 78.65% of Python3 online submissions

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        return max(count, key=count.get)
