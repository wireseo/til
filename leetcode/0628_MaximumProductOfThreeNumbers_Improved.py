# knowledge: heapq.nlargest(n, lst), heapq.nsmallest(n, lst)
# concepts: X
# comment: use heaps to skip sorting
# runtime: X, not mine
# memory usage: X, not mine

def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])