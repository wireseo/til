# knowledge: tuple() to create tuple
# concepts: two pass, min array
# comment: need to memorize two pass method
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        minArr = [n] * n
        pos = -n
        for i in tuple(range(n)) + tuple(range(n)[::-1]):
            if s[i] == c:
                pos = i
            minArr[i] = min(minArr[i], abs(i - pos))
        return minArr