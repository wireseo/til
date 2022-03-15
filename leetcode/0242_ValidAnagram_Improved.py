# knowledge: collecions.Counter() holds the count of each of the elements present in the container
    # defaultdict(int) keys are null-safe
# concepts: anagram
# comment: may not be what the interviewer is looking for, but are good pythonic solutions
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            return collections.Counter(s) == collections.Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())