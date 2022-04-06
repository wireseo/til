# knowledge: dictionaries are ordered from Python 3.6
# concepts: dictionaries
# comment: need to know to use ordered dictionary for elegant solution!
    # also converting string from list after all operations is more efficient than appending to a string
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        res = []
        
        for i in d:
            res.append((num // i) * d[i])
            num %= i
        
        return ''.join(res)