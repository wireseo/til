# knowledge: X
# concepts: recursion
# comment: can memorize recursive approach to converting to base n
# runtime: X, not mine
# memory usage: X, not mine

def convertToBase7(self, num: int) -> str:
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7: return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)