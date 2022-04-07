# knowledge: min(max(min, number), max), abs(), <<1 = * 2
# concepts: integer manipulation
# comment: way to speed up dividing with bit operation
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            curr_divisor, num_divisors = divisor, 1
            while dividend >= curr_divisor:
                dividend -= curr_divisor
                quotient += num_divisors
                
                curr_divisor = curr_divisor << 1
                num_divisors = num_divisors << 1
        
        quotient = -quotient if is_negative else quotient
        return min(max(-2**31, quotient), 2**31-1)
    