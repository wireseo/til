# knowledge: string.upper()
# concepts: string manipulation
# comment: reverse is inevitable, but try using generator for string manipulation questions
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]