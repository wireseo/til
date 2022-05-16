# knowledge: X
# concepts: set
# comment: easy question
# runtime: 47 ms, faster than 52.30% of Python3 online submissions
# memory usage: 13.8 MB, less than 98.79% of Python3 online submissions

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        charToMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        setOfCode = set()

        for word in words:
            transformation = []
            for char in word:
                transformation.append(charToMorse[ord(char) - 97])
            setOfCode.add(''.join(transformation))
            
        return len(setOfCode)