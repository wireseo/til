# knowledge: X
# concepts: Floyd's tortoise and hare algorithm (fast and slow pointers)
# comment: use tortoise and hare for "find inner loop" problems
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isHappy(self, n: int) -> bool:
        # helper function to get sum of squared numbers
        def squared(n):
            return sum(int(i) ** 2 for i in str(n))

        slow = squared(n)
        fast = squared(squared(n))

        while slow != fast and fast != 1:
            slow = squared(slow)
            fast = squared(squared(fast))

        return fast == 1

        
