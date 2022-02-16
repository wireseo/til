# knowledge: self.~~(), list.extend(), [] + list (simply adds new item to list!)
    # range(start, stop, step)
# concepts: recursion
# comment: X
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def plusOne(self, digits):
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits