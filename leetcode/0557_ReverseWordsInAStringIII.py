# knowledge: X
# concepts: reversing string, string manipulation
# comment: easy question; but should know how to write reverse function on my own to be safe
# runtime: 46 ms, faster than 73.51% of Python3 online submissions
# memory usage: 14.6 MB, less than 85.38% of Python3 online submissions

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        for idx in range(len(words)):
            words[idx] = words[idx][::-1]
        
        return ' '.join(words)
                