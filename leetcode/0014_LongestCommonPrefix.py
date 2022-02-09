# knowledge: enumerate()
# concepts: X
# comment: think more intuitively, understand the problem first
# runtime: 28 ms, faster than 96.75% of Python3 online submissions (28~61 ms)
# memory usage: 13.9 MB, less than 98.26% of Python3 online submissions

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        standard = strs[0]
        wordLength = len(standard)
        listLength = len(strs)
        longestPrefix = ""
        
        if listLength > 1 and wordLength > 0:
            for count, char in enumerate(standard):
                for str in strs[1:]:
                    if len(str) <= count or str[count] != char:
                        return longestPrefix
                longestPrefix += char
            return longestPrefix
        
        elif listLength == 1:
            return standard
        
        else:
            return longestPrefix
