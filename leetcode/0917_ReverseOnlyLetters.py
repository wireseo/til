# knowledge: isalpha()
# concepts: two pointer
# comment: easy question, is there an alternative solution?
# runtime: 36 ms, faster than 71.34% of Python3 online submissions
# memory usage: 13.9 MB, less than 62.73% of Python3 online submissions

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        lst = list(s)
        
        while left < right:
            if lst[left].isalpha():
                if lst[right].isalpha():
                    lst[left], lst[right] = lst[right], lst[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        
        return ''.join(lst)