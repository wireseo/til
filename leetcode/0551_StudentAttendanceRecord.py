# knowledge: X
# concepts: X
# comment: easy question, but maybe there is a simpler solution
# runtime: 38 ms, faster than 66.89% of Python3 online submissions
# memory usage: 13.8 MB, less than 96.74% of Python3 online submissions

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        
        consec = 0
        for c in s:
            if c == 'L':
                consec += 1
                if consec == 3:
                    return False
            else:
                consec = 0
                
        return True