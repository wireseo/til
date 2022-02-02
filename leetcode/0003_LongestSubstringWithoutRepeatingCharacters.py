# knowledge: ord(), string[idx], unicode array
# concepts: sliding window algorithm
# comment: could not attempt due to lacking knowledge of sliding window
    # or even the implementation of the brute force method
# runtime: X, had to search solution
# memory usage: X, had to search solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ord() = unicode code of given character
        # subchar can be found with string[index]
        
        chars = [0] * 128 # array of size 128 full of 0s, represent 
        left = right = 0
        curLongestLength = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1 # increment counter in unicode array for right char

            while chars[ord(r)] > 1: # while window contains r (when left char and right char are not the same index char)
                l = s[left]
                chars[ord(l)] -= 1 # decrement counter in unicode array for left char
                left += 1 # slide window to the left

            curLongestLength = max(curLongestLength, right - left + 1)
            right += 1 # sliding window to the right
            
        return curLongestLength