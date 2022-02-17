# knowledge: X
# concepts: binary search & finding return pattern
# comment: better stop with no unnecessary elements
# runtime: X, not mine
# memory usage: X, not mine

def mySqrt(self, x):
    lo, hi = 0, x
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if mid * mid > x:
            hi = mid - 1
        elif mid * mid < x:
            lo = mid + 1
        else:
            return mid
    
    # When there is no perfect square, hi is the the value on the left
    # of where it would have been (rounding down). If we were rounding up, 
    # we would return lo
    return hi