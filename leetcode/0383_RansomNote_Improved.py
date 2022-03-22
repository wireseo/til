# knowledge: X
# concepts: collections.Counter
# comment: usually counter is faster
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)