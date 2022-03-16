# knowledge: X
# concepts: mathematical induction
# comment: difficult brainteaser, must find pattern
# runtime: 28 ms, faster than 94.14% of Python3 online submissions
# memory usage: 13.7 MB, less than 96.85% of Python3 online submissions

class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1 --> True
        # 2 --> True
        # 3 --> True
        # 4 --> False
        # 5 --> True
        # 6 --> True
        # 7 --> True... if there is a way to reduce the number to 1,2,3,5,6 by your turn, you can win the game
        
        return n % 4 != 0 # all multiples of 4 would lose!