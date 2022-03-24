# knowledge: X
# concepts: palindrome counting
# comment: may be better way of handling hasLeftover
# runtime: 50 ms, faster than 43.39% of Python3 online submissions
# memory usage: 13.9 MB, less than 73.77% of Python3 online submissions

class Solution:
    def longestPalindrome(self, s: str) -> int:
        lengthOfPalindrome = 0
        hasLeftover = False
        
        # even pair of case sensitive letters adds 2 to length
        counter = collections.Counter(s)
        for letter in counter:
            while counter[letter] > 1:
                counter[letter] -= 2
                lengthOfPalindrome += 2
            if not hasLeftover and counter[letter] >= 1:
                hasLeftover = True
        
        # if string is not empty after removing case sensitive letter pairs, add 1 to lengthOfPalindrome
        if hasLeftover:
            lengthOfPalindrome += 1
        
        return lengthOfPalindrome