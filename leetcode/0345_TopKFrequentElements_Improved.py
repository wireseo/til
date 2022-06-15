# knowledge: itertools.chain() = chain lists together
    # * = splat operator, takes list and separates its elements out to be the actual positional arguments
# concepts: bucket sort
# comment: X
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        
        for num, freq in Counter(nums).items():
            bucket[-freq].append(num)
            
        return list(itertools.chain(*bucket))[:k] 
