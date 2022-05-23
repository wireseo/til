# knowledge: X
# concepts: counter, generator
# comment: need to utilize either & or - to create generator
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = Counter(x for x in licensePlate.lower() if x.isalpha())
        return min([w for w in words if not d - Counter(w)], key = len)