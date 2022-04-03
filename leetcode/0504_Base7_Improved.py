# knowledge: string * boolean = string printed only when boolean is true
# concepts: iteration
# comment: faster than recursive solution; should also memorize this version where you append % n first then divide by 7
# runtime: X, not mine
# memory usage: X, not mine

def convertToBase7(self, num: int) -> str:    
    if not num:
        return '0'
    
    sign = num < 0
    num = abs(num)
    
    stack = []
    while num:
        stack.append(str(num % 7))
        num = num // 7
    
    return '-' * sign + ''.join(stack[::-1])
