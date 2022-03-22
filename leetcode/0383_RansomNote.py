# knowledge: X
# concepts: dictionaries
# comment: easy dict question
# runtime: 72 ms, faster than 67.41% of Python3 online submissions
# memory usage: 14 MB, less than 95.32% of Python3 online submissions

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        
        for letter in magazine:
            if letter in magDict:
                magDict[letter] += 1
            else:
                magDict[letter] = 1
        
        for letter in ransomNote:
            if letter in magDict and magDict[letter] > 0:
                magDict[letter] -= 1
            else:
                return False
            
        return True