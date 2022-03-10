# knowledge: for pair in zip(x,y)
# concepts: utilizing sets and dicts
# comment: seems like there would be a more efficient approach to this problem... maybe tuple in set?
# runtime: 65 ms, faster than 42.08% of Python3 online submissions
# memory usage: 14.2 MB, less than 63.07% of Python3 online submissions

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # all occurrences must be changed to the same char
        # thus need to check if all char mapping is the same
        # all keys and values should be distinct
        
        charMap = {} # s.char --> t.char; 'P': 'E' etc. 
        valueSet = set()
        
        for charSet in zip(s, t):
            if charSet[0] in charMap:
                if not charMap.get(charSet[0]) == charSet[1]:
                    return False
            elif charSet[1] in valueSet:
                return False
            else:
                charMap[charSet[0]] = charSet[1]
                valueSet.add(charSet[1])
        
        return True
        