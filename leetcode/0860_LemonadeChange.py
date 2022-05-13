# knowledge: X
# concepts: dict
# comment: is there a faster way?
# runtime: 1173 ms, faster than 34.61% of Python3 online submissions
# memory usage: 17.8 MB, less than 71.94% of Python3 online submissions

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashier = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            if bill == 5:
                cashier[5] += 1
            elif bill == 10:
                if cashier[5] != 0:
                    cashier[5] -= 1
                    cashier[10] += 1
                else:
                    return False
            else:
                if cashier[5] > 0 and cashier[10] > 0:
                    cashier[5] -= 1
                    cashier[10] -= 1
                    cashier[20] += 1
                elif cashier[5] > 2:
                    cashier[5] -= 3
                    cashier[20] += 1
                else:
                    return False
                
        return True