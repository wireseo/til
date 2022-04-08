# knowledge: X
# concepts: fibonacci, recursive
# comment: brute force; might want to conserve space with binary tree? (= "memoized" recursive)
# runtime: 931 ms, faster than 16.84% of Python3 online submissions
# memory usage: 13.9 MB, less than 58.68% of Python3 online submissions

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)