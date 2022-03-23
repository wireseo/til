# knowledge: you can subtract a counter from another counter
# concepts: X
# comment: need to find faster method of getting the diff
# runtime: 54 ms, faster than 45.26% of Python3 online submissions
# memory usage: 13.9 MB, less than 36.11% of Python3 online submissions

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = collections.Counter(t) - collections.Counter(s)
        
        for char in diff:
            if diff[char] == 1:
                return char

    # 37 ms (79.66%) / 14 MB (36.11%)
    def findTheDifference(self, s: str, t: str) -> str:
        counter = collections.Counter(s)
        
        for char in t:
            if char in counter and counter[char] != 0:
                counter[char] -= 1
            else:
                return char