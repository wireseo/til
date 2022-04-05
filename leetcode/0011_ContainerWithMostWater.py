# knowledge: X
# concepts: two pointer
# comment: easier than I thought it would be, but too much memory usage
# runtime: 654 ms, faster than 98.95% of Python3 online submissions
# memory usage: 27.6 MB, less than 17.93% of Python3 online submissions

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # shorter vertical val * difference in idx 
        start, end = 0, len(height) - 1
        maxArea = 0
        
        while start < end:
            shorterVerticalLength = min(height[start], height[end])
            maxArea = max(maxArea, shorterVerticalLength * (end-start))
            
            if shorterVerticalLength == height[start]:
                i = start + 1
                while height[i] < height[start] and i < end:
                    i += 1
                start = i
            else:
                i = end - 1
                while height[i] < height[end] and i > start:
                    i -= 1
                end = i
                
        return maxArea