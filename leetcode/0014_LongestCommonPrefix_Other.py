# knowledge: list.sort(), zip() --> multi-iterate together, *: unpacks for function call
# concepts: sorting and only comparing first and last elements / set properties
# comment: more innovative thinking & approaches needed
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        if len(strs) == 1: 
            return strs[0]
        
        strs.sort()
        prefix = ""

        for x, y in zip(strs[0], strs[-1]):
            if x == y: 
                prefix += x
            else: 
                break

        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0

        for i in zip(*strs):
            if(len(set(i)) == 1):
                index += 1
            else:
                break

        return strs[0][:index]