# knowledge: X
# concepts: map
# comment: X, simple solution
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))