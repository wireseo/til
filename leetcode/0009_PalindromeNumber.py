# knowledge: a[::-1] = reverse the array/string
# concepts: X
# comment: used previous knowledge to solve efficiently and fast! 
    # but should try solving without converting it to string
# runtime: 100ms, faster than 32.90% of Python3 online submissions
# memory usage: 13.8 MB, less than 99.56% of Python3 online submissions

class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        return res[::-1] == res