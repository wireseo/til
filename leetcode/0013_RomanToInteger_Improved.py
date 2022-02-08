# knowledge: reversed()
# concepts: 'ordered dictionaries', finding patterns to take advantage of
# comment: try to make dictionaries and such more readable
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def romanToInt(self, s: str) -> int:
        # assuming python 3.6 with ordered dictionaries
        letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        # parse number right-to-left; remember biggest; if smaller is encountered, subtract
        max = 1
        sum = 0
        for l in reversed(s):
            val = letters[l]
            if val < max:
                sum -= val
            else:
                sum += val
            max = max(max, val)
        
        return sum