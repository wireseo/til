# knowledge: X
# concepts: binary search template
# comment: knew I had to use binary search but had a hard time implementing it properly
    # need to memorize template here https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
# runtime: X, not mine
# memory usage: X, not mine

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# template: 
# 1. Correctly initialize the boundary variables left and right. Set up the boundary to include all possible elements.
# 2. Decide return value. Is it return left or return left - 1? 
    #  Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function.
# 3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left