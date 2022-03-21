# knowledge: X
# concepts: Binary search
# comment: relatively easy problem, but need to set end/start conditions correctly
# runtime: 33 ms, faster than 74.02% of Python3 online submissions
# memory usage: 13.9 MB, less than 31.38% of Python3 online submissions

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            mid = start + (end - start) // 2
            guessed = guess(mid)
            
            if guessed == 0:
                return mid
            elif guessed == 1:
                start = mid + 1
            else:
                end = mid