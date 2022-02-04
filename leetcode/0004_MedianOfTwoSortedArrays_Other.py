# knowledge: sorted(): sorts array time efficiently
# concepts: X
# comment: need to have better understanding of existing python functions
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        if len(combined) % 2 == 1:
            return combined[len(combined) // 2]
        if len(combined) % 2 == 0:
            return (combined[len(combined) // 2] + combined[(len(combined) // 2)-1])/2