# knowledge: list(map()) to return list from map function
# concepts: map()
# comment: what I wanted to do, but clearer; utilize map & zip function
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))

        return map(dict(zip(sort, rank)).get, score)