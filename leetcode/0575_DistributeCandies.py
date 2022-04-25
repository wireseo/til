# knowledge: X
# concepts: set
# comment: good quick intuitive solution! can do one-liner by replacing variables with their definitions
# runtime: 835 ms, faster than 84.65% of Python3 online submissions
# memory usage: 16.3 MB, less than 41.35% of Python3 online submissions

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        maxCandies = len(candyType) // 2        
        uniqueCandies = set(candyType)
        
        return min(len(uniqueCandies), maxCandies)