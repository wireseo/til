# knowledge: X
# concepts: n-ary
# comment: bit manipulation
# runtime: X, not mine
# memory usage: X, not mine

# Definition for singly-linked list.
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return '0'
        
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15       # this means num & 1111b
            c = mp[n]          # get the hex char 
            ans = c + ans
            num = num >> 4
            
        return ans.lstrip('0')  #strip leading zeroes