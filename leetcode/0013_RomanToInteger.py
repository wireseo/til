# knowledge: python for vs while, range()
# concepts: reversing for easier computation, python dictionaries
# comment: not a very difficult problem, but how to make it faster?
# runtime: 90 ms, faster than 16.01% of Python3 submissions
# memory usage: 14 MB, less than 87.37% of Python3 submissions

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if len(s) > 0:
            reverse = s[::-1]
            sum = dict[reverse[0]]
        
            for i in range(1, len(reverse)):
                cur = reverse[i]
                prev = reverse[i - 1]

                if (prev == 'V' or prev == 'X') and cur == 'I':
                    sum -= 1
                elif (prev == 'L' or prev == 'C') and cur == 'X':
                    sum -= 10
                elif (prev == 'D' or prev == 'M') and cur == 'C':
                    sum -= 100
                else:
                    sum += dict[cur]
            
        return sum