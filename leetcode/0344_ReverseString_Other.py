# knowledge: ~i = -i-1
# concepts: two pointer method
# comment: one liner solution / one liner bitwise solution
# runtime: X
# memory usage: X

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]

    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]