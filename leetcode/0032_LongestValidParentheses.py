# knowledge: range(start, end, step)
# concepts: parentheses (dp, left/right, stack, etc.)
# comment: do both forward and backward passes to check valid p
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxLength = 0, 0, 0
        
        for i in range(len(s)):
            if s[i] == '(': left += 1
            else: right += 1
                
            if left == right:
                maxLength = max(maxLength, left + right);
            elif right >= left:
                left = right = 0
            
        
        left = right = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '(': left += 1
            else: right += 1
                
            if left == right:
                maxLength = max(maxLength, left + left)
            elif left >= right:
                left = right = 0
            
        return maxLength