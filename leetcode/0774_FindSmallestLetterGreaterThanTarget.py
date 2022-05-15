# knowledge: X
# concepts: X
# comment: easy question
# runtime: 123 ms, faster than 68.13% of Python3 online submissions
# memory usage: 14.4 MB, less than 62.84% of Python3 online submissions

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(target) < ord(letter):
                return letter
        
        return letters[0]