# knowledge: X
# concepts: fibonacci, recursive, memoization, cache
# comment: need to study concept of least recently used cache
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    # recursive space optimized
    memo = {}
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1

        if N-1 not in memo: memo[N-1] = fib(N-1)
        if N-2 not in memo: memo[N-2] = fib(N-2)

        return memo[N-1] + memo[N-2]

    # iterative space optimized
    def fib(N):
        if N == 0: return 0

        memo = [0,1]
        for _ in range(2,N+1):
            memo = [memo[-1], memo[-1] + memo[-2]]
            
        return memo[-1]

    # keep loading on a
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for _ in repeat(None, n):
            a, b = b, a+b

        return a


    # from functools import lru_cache
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)