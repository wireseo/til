# knowledge: X
# concepts:  binary computation
# comment: finding binary patterns; very difficult, look at link for details
# runtime: 47 ms, faster than 50.76% of Python3 online submissions
# memory usage: 13.8 MB, less than 67.81% of Python3 online submissions

# https://leetcode.com/problems/power-of-two/discuss/1638707/PythonC%2B%2BJava-Detailly-Explain-Why-n-and-n-1-Works-oror-1-Line-oror-100-Faster-oror-Easy

class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)