# knowledge: Counter class
# concepts: unrepeated letter
# comment: good quick solution
# runtime: 57 ms, faster than 99.21% of Python3 online submissions
# memory usage: 14.2 MB, less than 67.99% of Python3 online submissions

class Solution:
    def firstUniqChar(self, s: str) -> int:        
        counter = collections.Counter(s)
        
        for letter in counter:
            if counter[letter] == 1:
                return s.find(letter)
        
        return -1