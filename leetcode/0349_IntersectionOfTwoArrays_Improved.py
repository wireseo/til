# knowledge: set.add(), set operations:
    # intersection (&), difference (-), union (|), symmetric difference (^)
# concepts: sets and intersections
# comment: can use inbuilt set operations as above
# runtime: X
# memory usage: X

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set2 & set1)