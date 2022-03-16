# knowledge: X
# concepts: dictionaries
# comment: remember to check if values exist in the dict along with the key; all values must be unique to the key
# runtime: 28 ms, faster than 94.33% of Python3 online submissions
# memory usage: 13.8 MB, less than 94.09% of Python3 online submissions

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        bijectionMap = {}
        strings = s.split(' ')
        
        if len(pattern) != len(strings):
            return False
        
        for idx, char in enumerate(pattern):
            if char not in bijectionMap:
                if strings[idx] not in bijectionMap.values():
                    bijectionMap[char] = strings[idx]
                else:
                    return False
            else:
                if bijectionMap[char] != strings[idx]:
                    return False
        
        return True