# knowledge: heapq for max heaps (multiply -1)
# concepts: priority queues / heaps
# comment: X
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap) # for max heap
        
        while len(maxHeap) > 1 and maxHeap[0] != 0:
            heapq.heappush(maxHeap, heapq.heappop(maxHeap) - heapq.heappop(maxHeap))
            
        return -1 * maxHeap[0]