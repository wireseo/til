# knowledge: reversed(range(len())), insert()
# concepts: X
# comment: insert doesn't return anything; return somewhere else
    # need to manipulate data itself with list[i] rather than enumerate
    # carryOn --> carry (simple naming)
# runtime: 54 ms, faster than 27.38% of Python3 online submissions
# memory usage: 13.8 MB, less than 99.17% of Python3 online submissions

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate reversed array, add one, if larger than 9 increment carry-on
        carryOn = 1
        
        for i in reversed(range(len(digits))):
            if carryOn > 0:
                digits[i] += carryOn
                carryOn = 0
            
            if digits[i] > 9:
                digits[i] -= 10
                if i == 0: # if this is the first leading digit
                    digits.insert(0, 1)
                else:
                    carryOn += 1
        
        return digits