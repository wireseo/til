# knowledge: X
# concepts: stacks and queues
# comment: need to consider both push/pop operations to alter
# runtime: 20 ms, faster than 99.76% of Python3 online submissions
# memory usage: 14 MB, less than 84.58% of Python3 online submissions

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1