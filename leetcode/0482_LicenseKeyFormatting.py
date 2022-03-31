# knowledge: string.capitalize(), string.switchCase()
# concepts: string manipulation
# comment: too complicated & inefficient; should be much more concise
# runtime: 83 ms, faster than 46.53% of Python3 online submissions
# memory usage: 17.6 MB, less than 10.25% of Python3 online submissions

class Solution:
    # is this better than removing dashes first?
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # go through string backwards
        # if meet dash, remove it (and don't count i towards k), convert all non-dashes to caps
        # insert dash when i == k 
        
        i = 0
        result = []
        
        for c in enumerate(reversed(s)):
            if i == k: # should not add dash if it is the first letter of result string
                i = 0
                result.append("-")
                
            if c != '-':
                i += 1
                result.append(c.capitalize())
                
        if len(result) == 0:
            return ""
        else:
            return ''.join(result)[:-1:] if result[-1] == '-' else ''.join(result)[::-1]