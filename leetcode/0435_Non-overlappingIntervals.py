# knowledge: lambda x: x something, float('-inf')
# concepts: greedy algorithm
# comment: less is more!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, count = float('-inf'), 0
        
        for s, e in sorted(intervals, key=lambda x: x[1]): # sort by end time
            if s >= end: 
                end = e
            else: 
                count += 1

        return count