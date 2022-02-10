# knowledge: stack.pop(), stack.append(), using list as stack
# concepts: using stacks
# comment: use stacks when LIFO is required
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(": ")", "[": "]",  "{": "}"}
        stack = []

        for i in s:
            if i in m:
                stack.append(i)
            elif stack and i == m[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []