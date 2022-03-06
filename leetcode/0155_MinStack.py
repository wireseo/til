# knowledge: X
# concepts: Creating class & methods
# comment: Use list, don't make node! Also store min value in every element with mini list
    # why is tuple slower than using list (although it uses less memory)? 
# runtime: X, not mine
# memory usage: X, not mine

class MinStack:
    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        if len(self.stack) > 1: 
            self.stack.pop()

    def top(self):
        if len(self.stack) == 1: 
            return None
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]