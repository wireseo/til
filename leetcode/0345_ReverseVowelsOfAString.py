# knowledge: X
# concepts: two pointer method
# comment: strings are immutable in python, need to convert to list 
    # or use replace for in-place modification; also can swap values with A,B=B,A
# runtime: 68 ms, faster than 71.33% of Python3 online submissions
# memory usage: 15.1 MB, less than 64.39% of Python3 online submissions

class Solution:
    def reverseVowels(self, s: str) -> str:
        front,end = 0, len(s) - 1
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        strLst = list(s)
        
        while front < end:
            if strLst[front] in vowels and strLst[end] in vowels:
                strLst[front], strLst[end] = strLst[end], strLst[front]
                front += 1
                end -= 1
            if strLst[front] not in vowels:
                front += 1
            if strLst[end] not in vowels:
                end -= 1

        return "".join(strLst)
        