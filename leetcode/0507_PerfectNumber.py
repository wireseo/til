# knowledge: X
# concepts: X
# comment: good solution, don't forget to check case for only adding one num if sqrt ^ 2 == num
    # may additionally want to look into Euclid-Euler Theorem
# runtime: 49 ms, faster than 63.18% of Python3 online submissions
# memory usage: 13.8 MB, less than 59.88% of Python3 online submissions

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        lst = []
        
        for x in range(1, int(sqrt(num)) + 1):
            if num % x == 0:
                lst.append(x)
                if x != num / x:
                    lst.append(num / x)

        return sum(lst) - num == num