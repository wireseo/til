# knowledge: split()
# concepts: string manipulation
# comment: why was this so difficult???
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
    
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count