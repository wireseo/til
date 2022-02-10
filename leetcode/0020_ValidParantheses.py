# knowledge: reversed(list(enumerate(__))), remove char from string with substring
# concepts: finding valid pairs from string
# comment: need to find more efficient core algorithms
# runtime: 2152 ms, faster than 5.41% of Python3 online submissions
# memory usage: 29.5 MB, faster than 5.82% of Python3 online submissions

class Solution:
    def recursiveScan(self, s: str, d: dict) -> bool:
        # string length cannot be odd
        if len(s) % 2 == 1:
            return False
        
        # cannot start with closing paranthesis
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        
        # identify first pair (returns index of closing paranthesis)
        closingIdx = -1
        openingOccurrence = 0
        for i, c in enumerate(s[1:]):
            # loop until valid closing occurs
            if s[0] == c:
                openingOccurrence += 1

            elif d[s[0]] == c:
                if openingOccurrence == 0:
                    closingIdx = i
                    break
                else:
                    openingOccurrence -= 1

        if closingIdx == -1 or closingIdx % 2 == 1: # if not found or odd position
            return False
        if closingIdx == 0 and len(s) == 2: # if is a complete pair
            return True
        else: # remove pair from string
            s = s[1:closingIdx+1] + s[(closingIdx+2):]
            return self.recursiveScan(s, d)
        
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        
        return self.recursiveScan(s, d)
        