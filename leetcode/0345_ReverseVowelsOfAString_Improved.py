# knowledge: X
# concepts: two pointer method
# comment: use set instead of list to store vowels, left/right variable name better than front/end
    # better use of while loops
# runtime: X
# memory usage: X

class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vowels = set('aeiouAEIOU')
        l, r = 0, len(s) - 1

        while l <= r:
            while l <= r and s[l] not in vowels: l += 1
            while l <= r and s[r] not in vowels: r -= 1

            if l > r: break
            
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

        return ''.join(s)