# knowledge: X
# concepts: binary search & finding return pattern
# comment: as always, determining the stop point and increments is difficult
# runtime: 63 ms, faster than 40.62% of Python3 online submissions
# memory usage: 13.8 MB, less than 98.93% of Python3 online submissions

class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search between 1 and x
        low = 0
        high = x
        
        while low < high:
            midpoint = (low + high) // 2
            if midpoint * midpoint == x:
                return midpoint
            elif midpoint * midpoint > x:
                if (midpoint - 1) * (midpoint - 1) <= x:
                    return midpoint - 1
                else:
                    high = midpoint
            else:
                if (midpoint + 1) * (midpoint + 1) > x:
                    return midpoint
                else:
                    low = midpoint + 1
        
        return x