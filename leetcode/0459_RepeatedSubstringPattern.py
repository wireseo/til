# knowledge: X
# concepts: string manipulation
# comment: how do I even start to attempt these mindbending problems? :/
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
    # First char of input string is first char of repeated substring
    # Last char of input string is last char of repeated substring
    # Let S1 = S + S (where S in input string)
    # Remove first and last char of S1. Let this be S2
    # If S exists in S2 then return true else false
    # Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1