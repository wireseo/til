# knowledge: list(d.values())
# concepts: dictionary
# comment: think of using a dictionary when seeing something that can be "grouped" into a same key
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            d[key] = d.get(key, []) + [word]
        return list(d.values())
        