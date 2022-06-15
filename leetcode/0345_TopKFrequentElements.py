# knowledge: Counter().most_common(k)
# concepts: X
# comment: can use bucket sort to improve on time efficiency
# runtime: 147 ms, faster than 49.25% of Python3 online submissions
# memory usage: 18.7 MB, less than 69.30% of Python3 online submissions

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for k,v in Counter(nums).most_common(k)]
    