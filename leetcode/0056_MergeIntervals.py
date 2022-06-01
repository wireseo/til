# knowledge: lambda x: ~,  looking at previously inserted item of array by -1
# concepts: intervals
# comment: you can edit previously inserted item through -1
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        
        for i in intervals[1:]:
            if merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[-1])
                
        return merged