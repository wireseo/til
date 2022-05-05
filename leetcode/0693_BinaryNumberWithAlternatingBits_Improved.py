# knowledge: >>, &
# concepts: bit manipulation
# comment: need to memorize some of these neat tricks
# runtime: 32 ms, faster than 82.22% of Python3 online submissions
# memory usage: 13.8 MB, less than 95.63% of Python3 online submissions

class Solution:
    def bitSolution(number):
    #       10101010101
    #   +    1010101010    ( number >> 1 )
    #   ---------------
    #   =   11111111111
    #   &  100000000000
    #   ---------------
    #   =             0    ( power of two )
        tmp = ( number >> 1 ) + number
        return (tmp & tmp + 1) == 0
