# knowledge: X
# concepts: Dict
# comment: X, easy
# runtime: 30 ms, faster than 87.59% of Python3 online submissions
# memory usage: 13.9 MB, less than 20.35% of Python3 online submissions

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphaDict = {'a': 2, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 
                     'j': 2, 'k': 2, 'l': 2, 'm': 3, 'n': 3, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 
                     's': 2, 't': 1, 'u': 1, 'v': 3, 'w': 1, 'x': 3, 'y': 1, 'z': 3}
        rslt = []
        
        for word in words:
            passed = True
            target = alphaDict[word[0].lower()]
            
            for c in word:
                if alphaDict[c.lower()] != target:
                    passed = False
            if passed: rslt.append(word)
            
        return rslt