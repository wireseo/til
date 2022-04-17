# knowledge: X
# concepts: X
# comment: too easy, but is there a way to make it shorter?
# runtime: 49 ms, faster than 87.5% of Python3 online submissions
# memory usage: 14.2 MB, less than 5.58% of Python3 online submissions

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # as long as they are all paired up
        x_axis, y_axis = 0, 0
        
        for move in moves:
            if move == 'L':
                x_axis += 1
            elif move == 'R':
                x_axis -= 1
            elif move == 'U':
                y_axis += 1
            elif move == 'D':
                y_axis -= 1
        
        return x_axis == 0 and y_axis == 0