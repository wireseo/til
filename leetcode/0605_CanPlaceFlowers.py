# knowledge: X
# concepts: X
# comment: can place one flower every three empty spots! use counter rather than checking i+1 and i-1
# runtime: X, not mine
# memory usage: X, not mine

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):		
        flowerbed.append(0)
        count = 1
        
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return True
            
        return False