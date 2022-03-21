# knowledge: X
# concepts: number manipulation
# comment: need to memorize some of these methods (Newton/Bitwise best solutions)
# runtime: X
# memory usage: X

class Solution:
    def BitwiseTrick(self, num):
       root = 0
       bit = 1 << 15
       
       while bit > 0 :
           root |= bit
           if root > num // root:    
               root ^= bit                
           bit >>= 1        
       return root * root == num

    def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num

    def Math(self, num):
        i = 1
        while (num>0):
            num -= i
            i += 2       
        return num == 0

    def BinarySearch(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False