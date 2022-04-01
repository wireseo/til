# knowledge: sqrt(), range(start, end, direction)
# concepts: area calculation
# comment: not bad, but taking up too much memory for some reason
# runtime: 52 ms, faster than 54.66% of Python3 online submissions
# memory usage: 13.9 MB, less than 12.11% of Python3 online submissions

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrtAsInt = int(sqrt(area))
        
        for width in range(sqrtAsInt, 0, -1):
            length = area/width
            if length % 1 == 0:
                return [int(length), width]
        