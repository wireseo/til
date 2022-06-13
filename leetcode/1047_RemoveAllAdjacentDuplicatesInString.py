# knowledge: stack[-1] to peek
# concepts: greedy algo, stacks
# comment: use stacks for these questions
# runtime: 73 ms, faster than 92.47% of Python3 online submissions
# memory usage: 14.8 MB, less than 47.07% of Python3 online submissions

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
            
        return ''.join(stack)