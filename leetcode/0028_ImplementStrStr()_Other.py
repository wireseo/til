# knowledge: X
# concepts: use python array method instead of two pointers
# comment: simple and intuitive
# runtime: X
# memory usage: X

class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1