# knowledge: X
# concepts: two pointers
# comment: again with the looping. need to practice how to solve looping elegantly without getting confused
# runtime: X
# memory usage: X

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        # find first char in string, then check further strings
        for i in range(len(haystack)):
            print('i ', i)
            if haystack[i] is needle[0]:
                flag = True
                j = i + 1
                while j < len(haystack) and (j - i) < len(needle) and flag:
                    print(j-i)
                    if haystack[j] != needle[j - i]:
                        flag = False
                    j += 1
                if flag:
                    return i

        return -1