# knowledge: set.add()
# concepts: sets and intersections
# comment: can use less sets than this
# runtime: 48 ms, faster than 87.76% of Python3 online submissions
# memory usage: 14.1 MB, less than 77.17% of Python3 online submissions

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        out = set()
        
        for num in set1:
            if num in set2:
                out.add(num)
                
        return out