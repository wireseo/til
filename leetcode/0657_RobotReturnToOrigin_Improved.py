# knowledge: list.count('<someString>')
# concepts: X
# comment: compare with count function
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))
