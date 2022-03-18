# knowledge: X
# concepts: two pointer method
# comment: classic two-pointer version
# runtime: 231 ms, faster than 68.27% of Python3 online submissions
# memory usage: 8.5 MB, less than 56.94% of Python3 online submissions

class Solution:
    def reverseString(self, s: List[str]) -> None:
        front = 0
        end = len(s) - 1
        
        while front < end:
            temp = s[front]
            s[front] = s[end]
            s[end] = temp
            
            front += 1
            end -= 1
        