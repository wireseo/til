# knowledge: X
# concepts: ?
# comment: greedy algorithm? need to sort first though 
    # GA: problem-solving heuristic of making the locally optimal choice at each stage.
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        childCount, cookieCount = 0, 0
        
        g.sort()
        s.sort()
        
        while cookieCount < len(s) and childCount < len(g):
            if s[cookieCount] >= g[childCount]:
                childCount += 1
            cookieCount += 1
        
        return childCount